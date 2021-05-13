import sys

sys.setrecursionlimit(10 ** 6)


def dfs(idx):
    for x in arr[idx]:
        if not vis[x]:
            vis[x] = True
            dfs(x)


n, m = map(int, input().split())

arr = [[] * (n + 1) for _ in range(n + 1)]
vis = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

ans = 0

if m == 0:
    print(n-1)
    sys.exit()

dfs(1)
for i in range(2, n + 1):
    if not vis[i]:
        vis[i] = True
        dfs(i)
        ans += 1

print(ans)
