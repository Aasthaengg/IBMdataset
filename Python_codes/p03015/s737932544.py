L = input()
MOD = 10**9 + 7
ans = 1
for i in range(1, len(L)+1):
    if L[-i] == "1":
        ans = ans * 2 % MOD
        ans += pow(3,i-1,MOD)
        ans %= MOD
print(ans)