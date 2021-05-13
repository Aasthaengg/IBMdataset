from collections import Counter

n = int(input())
S = input()
mod = 10**9+7

n = Counter(S)
ans = 1
for i, j in n.items():
  ans *= (j+1)
print((ans-1)%mod)
