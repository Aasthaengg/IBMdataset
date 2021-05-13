import collections

n = int(input())
a = input()
ans = 1
mod = 10**9+7
a = collections.Counter(a)
for v in a.values():
    ans *= (v+1) % mod
print((ans-1) % mod)
