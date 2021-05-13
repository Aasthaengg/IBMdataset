n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))
p = 0
ans = 0
f = []
g = [0] * n
for i, x in enumerate(b):
    while p < n and x >= c[p]:
        p += 1
    f.append(n - p)
for i in range(n - 1, -1, -1):
    g[i] = f[i] + (g[i + 1] if i < n - 1 else 0)
p = 0
for i, x in enumerate(a):
    while p < n and x >= b[p]:
        p += 1
    ans += g[p] if p < n else 0
print(ans)
