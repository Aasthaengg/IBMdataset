import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))

edges = defaultdict(lambda: [])
used = [False for _ in range(1001000)]
d = [1 for _ in range(1001000)]


def dfs(i):
    if used[i]:
        return d[i]
    else:
        used[i] = True
        ret = 0
        for v in edges[i]:
            tmp = dfs(v)
            if ret < tmp+1:
                ret = tmp+1
        d[i] = ret
        return ret


def main():
    n = int(input())
    h = [0 for _ in range(1001000)]
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(1, n-1):
            pa = a[j-1]-1
            na = a[j]-1
            pi = i
            ni = i
            if na > ni:
                na, ni = ni, na
            if pa > pi:
                pa, pi = pi, pa
            edges[1000*pi + pa].append(1000*ni + na)
            h[1000*ni + na] += 1
    
    stack = []
    for k, _ in edges.items():
        if h[k] == 0:
            stack.append(k)
    
    ans = 0
    while len(stack):
        u = stack.pop()
        for v in edges[u]:
            h[v] -= 1
            if h[v] == 0:
                stack.append(v)
        ans += 1

    if ans != n*(n-1)//2:
        print(-1)
    else:
        ret = 0
        for k, _ in edges.items():
            tmp = dfs(k)
            if tmp > ret:
                ret = tmp
        print(ret+1)


if __name__ == '__main__':
    main()
