N = int(input())
MOD = 10**9 + 7


N0 = 9 ** N % MOD
N9 = 9 ** N % MOD
NA = 10 ** N % MOD
NB = 8 ** N % MOD

ans = ( NA - (N0 + N9 - NB) ) % MOD
print(ans)