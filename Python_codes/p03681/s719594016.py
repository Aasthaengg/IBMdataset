MOD = 10 ** 9 + 7

kai = [1, 1]
for i in range(2, 10 ** 5 + 1):
    num = kai[-1] * i
    kai.append(num % MOD)
n, m = map(int, input().split())
if abs(n - m) > 1:
    ans = 0
else:
    ans = kai[n] * kai[m]
    if n == m:
        ans *= 2
    ans %= MOD
print(ans)