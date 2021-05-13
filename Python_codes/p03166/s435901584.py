from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def read():
    N, M = map(int, input().strip().split())
    parents = [list() for i in range(N)]
    n_children = [0 for i in range(N)]
    for i in range(M):
        x, y = map(int, input().strip().split())
        n_children[x-1] += 1  # x -> E_out[x]
        parents[y-1].append(x-1)   # E_in[x] -> x
    return N, M, n_children, parents


def solve(N, M, n_children, parents):
    dp = [0 for i in range(N)]
    q = deque()
    r = deque()
    for x in range(N):
        if n_children[x] == 0:
            q.append(x)
    while q:
        x = q.pop()
        r.append(x)
        for parent in parents[x]:
            n_children[parent] -= 1
            if n_children[parent] == 0:
                q.append(parent)
    
    while r:
        x = r.pop()
        for y in parents[x]:
            dp[x] = max(dp[x], dp[y]+1)
    return max(dp)


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
