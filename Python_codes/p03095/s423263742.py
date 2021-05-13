from collections import Counter

N = int(input())
S = input()
L = Counter(S)
MOD = 10**9 + 7

ans = 1
for k in L.keys():
    ans *= ((L[k]+1) % MOD)

print((ans-1)%MOD)
