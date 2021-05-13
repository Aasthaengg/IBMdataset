from collections import Counter

N = int(input())
S = input()

mod = 10**9+7

cnt = Counter(S)

res = 1
for v in cnt.values():
    res *= v+1
    res %= mod

print((res-1)%mod)