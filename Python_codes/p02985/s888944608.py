import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n, k = map(int, readline().split())


graph = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    cnt[a] += 1
    cnt[b] += 1
ans = 1

mod = 10 ** 9 + 7
kaidan = [1] * (10 ** 5 + 1)
gyaku = [1] * (10 ** 5 + 1)

for i in range(1, 10 ** 5 + 1):
    kaidan[i] = i * kaidan[i - 1] % mod
    gyaku[i] = pow(kaidan[i], mod - 2, mod)


def perm(k, i):
    if i > k:
        return 0
    return kaidan[k] * gyaku[k - i]


# dfs

stack = [1]
used = [False] * (n + 1)
while stack:
    v = stack.pop()
    used[v] = True
    if v == 1:
        ans *= k * perm(k - 1, cnt[v])
        ans %= mod
    else:
        ans *= perm(k - 2, cnt[v] - 1)
        ans %= mod
    for u in graph[v]:
        if used[u] == True:
            continue
        stack.append(u)

print(ans)
