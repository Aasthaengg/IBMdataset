mod = 10**9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
v1 = v2 = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]: v1 += 1
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]: v2 += 1
x1 = k * (k + 1) // 2
x2 = k * (k - 1) // 2
ans = ((v1 * x1) + (v2 * x2)) % mod
print(int(ans))