from collections import Counter
n = input()
mod = 10**9+7
s = list(Counter(list(input())).values())
an = 1
for i in s:
  an *= (i+1)%mod
print((an-1)%mod)