n, *a = map(int, open(0).read().split())
b = [0] * 60
ans = 0
for i in range(n):
    for j in range(60):
        ans += 2**j * (i - b[j] if a[i] >> j & 1 else b[j])
        ans %= 10**9 + 7
    for j in range(len(bin(a[i])) - 2):
        b[j] += a[i] >> j & 1
print(ans)