from collections import Counter
MOD = 1000000007
N = int(input())
S = input()

count = Counter(S)
ans = 1
for k, v in count.items():
    ans *= (v+1)
    ans %= MOD
print((ans - 1) % MOD)
