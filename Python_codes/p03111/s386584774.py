from itertools import product
N, A, B, C = map(int, input().split())
l = [int(input()) for i in range(N)]
INF = 10 ** 9
ans = INF

def calc(a, b, c):
    la, lb, lc = len(a), len(b), len(c)
    if la + lb + lc < 3 or 0 in (la, lb, lc): return INF
    sa, sb, sc = sum(a), sum(b), sum(c)
    t = 0
    return abs(sa-A) + abs(sb-B) + abs(sc-C) + (la+lb+lc-3) * 10

def dfs(n, a, b, c):
    global ans
    if n == N:
        ans = min(ans, calc(a, b, c))
        return
    dfs(n+1, a, b, c)
    dfs(n+1, a+[l[n]], b, c)
    dfs(n+1, a, b+[l[n]], c)
    dfs(n+1, a, b, c+[l[n]])

dfs(0, [], [], [])
print(ans)
