n = int(input())
g = [[] for _ in range(n ** 2)]
inv = [0] * (n ** 2)
for i in range(n):
    a = list(map(lambda x: int(x)-1, input().split()))
    for j in range(n - 2):
        p, q = min(i, a[j]), max(i, a[j])
        r, s = min(i, a[j + 1]), max(i, a[j + 1])
        g[p * n + q].append(r * n + s)
        inv[r * n + s] += 1
s = []
for i in range(n):
    for j in range(i + 1, n):
        if inv[i * n + j] == 0:
            s.append(i * n + j)
d = [0] * (n ** 2)
while s:
    p = s.pop()
    for node in g[p]:
        d[node] = max(d[node], d[p] + 1)
        inv[node] -= 1
        if inv[node] == 0:
            s.append(node)
for i in range(n):
    for j in range(i + 1, n):
        if inv[i * n + j] > 0:
            print(-1)
            exit(0)
print(max(d) + 1)
