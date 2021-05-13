from collections import Counter
N = int(input())
S = list(str(input()))
mod = 10**9+7
count = 1
cs = Counter(S)

for key,value in cs.items():
  count *= (value+1)

print((count-1)%mod)