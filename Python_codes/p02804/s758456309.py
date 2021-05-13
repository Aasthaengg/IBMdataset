n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
a.sort()
b = 1
ans = 0
for i in range(k - 1, n):
    ans += b * (a[i] - a[n - i - 1])
    ans %= mod
    b = (i + 1) * b
    c = i + 1 - (k - 1)
    b = pow(c, mod - 2, mod) * b % mod
print(ans)