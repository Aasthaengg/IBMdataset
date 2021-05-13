import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline()

n, m = [int(i) for i in input().split()]
e = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(i) - 1 for i in input().split()]
    e[x].append(y)

used = [False] * n
top = []


def dfs(i):
    if not used[i]:
        used[i] = True
        for j in e[i]:
            dfs(j)
        top.append(i)


for i in range(n):
    dfs(i)

ans = [0] * n
for i in reversed(top):
    for j in e[i]:
        ans[j] = max(ans[j], ans[i] + 1)
print(max(ans))
