from collections import Counter
n = int(input())
s = list(input())
mod = 10**9+7
c = Counter(s)
ans = 1
for v in c.values():
    ans *= v+1
    ans %= mod
print((ans-1)%mod)
