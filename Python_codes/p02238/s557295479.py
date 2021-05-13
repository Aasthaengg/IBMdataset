n = int(input())
link = {}

for i in range(n):
    a = list(map(int, input().split()))
    a.reverse()

    u, k = a.pop(), a.pop()
    link[u] = []
    for j in range(k):
        link[u] += [a.pop()]

d, f = {}, {}
t = 0


def dfs(u):
    global t
    t += 1
    d[u] = t

    for v in link[u]:
        if v not in d: dfs(v)

    if u not in f:
        t += 1
        f[u] = t


for u in range(1, n + 1):
    if u not in d: dfs(u)

for i in range(1, n + 1):
    print(i, d[i], f[i])

