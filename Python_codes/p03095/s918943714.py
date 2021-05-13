from collections import Counter
MOD = 10**9 + 7
N = int(input())
S = input()
count_si = Counter(S)
ans = 1
for v in count_si.values():
    ans = (ans * (v+1)) % MOD

print((ans-1)%MOD)
