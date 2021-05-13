mod = 10 ** 9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
comb = [1] * (n - k + 1)
for i in range(n - k):
    comb[i + 1] = (comb[i] * (k + i) * pow(i + 1, mod - 2, mod)) % mod
ans = 0
for i in range(n - k + 1):
    ans = (ans + a[k + i - 1] * comb[i]) % mod
    ans = (ans - a[i] * comb[-1 - i]) % mod
print(ans)