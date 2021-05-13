L = input()
n = len(L)

onecnt = 0
ans = 0

MOD = 10 ** 9 + 7

for i in range(n):
    if L[i] == '0':continue
    onecnt += 1
    rest = n - i - 1
    ans += pow(2, onecnt - 1, MOD) * pow(3, rest, MOD) % MOD
    ans %= MOD
ans += pow(2, onecnt, MOD)
print(ans % MOD)
