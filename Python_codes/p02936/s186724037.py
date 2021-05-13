import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, Q = mi()
    a, b = i2(N-1)
    p, x = i2(Q)

    d = [[] for i in range(N)]
    for i in range(N-1):
        d[a[i]-1].append(b[i]-1)
        d[b[i]-1].append(a[i]-1)

    child = [[] for i in range(N)]
    parent = [None]*N

    q = deque([0])
    while q:
        now = q.pop()
        for v in d[now]:
            if parent[now] == v:
                continue
            parent[v] = now
            q.appendleft(v)

    c = [0]*N
    for i in range(Q):
        c[p[i]-1] += x[i]

    @lru_cache(maxsize=None)
    def dfs(i):
        if parent[i] == None:
            return c[i]
        
        return c[i]+dfs(parent[i])

    print(*[dfs(i) for i in range(N)])

if __name__ == '__main__':
    main()
