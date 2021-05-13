import sys
sys.setrecursionlimit(500000)

n, q = map(int, input().split())
ab = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
add = [0]*n
for _ in range(q):
    pp, xx = map(int, input().split())
    add[pp-1] += xx


def dfs(v, p, value):
    value += add[v]
    ans[v] = value
    for c in ab[v]:
        if c == p:
            continue
        dfs(c, v, value)


ans = [0]*n
dfs(0, -1, 0)
print(*ans)
