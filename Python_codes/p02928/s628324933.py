mod = 10**9 + 7
n, k = map(int, input().split())

a = list(map(int, input().split()))

inside = [0] * n
outside = [0] * n

for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inside[i] += 1

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            outside[i] += 1

ans = 0
ans += sum(inside) * k
ans %= mod
ans += sum(outside) * k * (k - 1) // 2
ans %= mod
print(ans)
