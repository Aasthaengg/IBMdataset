s = int(input())
MOD = 10 ** 9 + 7
ans = 0
fact = [0] * 10000
fact[0], fact[1] = 1, 1
for i in range(2, 10000):
    fact[i] = (fact[i-1] * i) % MOD

def f(n, r):
    return fact[n] * pow(fact[n-r], MOD-2, MOD) * pow(fact[r], MOD-2, MOD)

for i in range(1, s//3+1):
    if i == 1:
        ans += 1
    else:
        m = s - i * 3
        ans += f(m+i-1, m)
        ans %= MOD
print(ans%MOD)