from collections import Counter
n = int(input())
s = input()
mod = 10**9+7

s_c = Counter(s)

ans = 1
for c in s_c.values():
    ans*=c+1
print((ans-1)%mod)