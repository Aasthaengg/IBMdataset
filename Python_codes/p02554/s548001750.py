MOD = 10 ** 9 + 7
n = int(input())
ans10 = 10
ans9 = 9
ans8 = 8
for i in range(n - 1):
    ans10 = ans10 * 10 % MOD
    ans9 = ans9 * 9 % MOD
    ans8 = ans8 * 8 % MOD
ans = (ans10 - ans9 - ans9 + ans8) % MOD
ans = (ans + MOD) % MOD
print(ans)
