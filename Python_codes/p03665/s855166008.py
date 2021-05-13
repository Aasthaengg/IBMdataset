MOD = 10 ** 9 + 7
n = 50
fact = [0 for _ in range(n)]
invfact = [0 for _ in range(n)]
fact[0] = 1
for i in range(1, n):
    fact[i] = fact[i - 1] * i % MOD

invfact[n - 1] = pow(fact[n - 1], MOD - 2, MOD)

for i in range(n - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD
def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * invfact[k] * invfact[n - k] % MOD

n, p = map(int, input().split())
a = list(map(int, input().split()))
even = 0
odd = 0
for num in a:
    if num % 2 == 1:
        odd += 1
    else:
        even += 1
ans = 0
if p == 0:
    for i in range(0, odd + 1, 2):
        ans += nCk(odd, i)
    ans *= 2 ** even
else:
    for i in range(1, odd + 1, 2):
        ans += nCk(odd, i)
    ans *= 2 ** even
print(ans)