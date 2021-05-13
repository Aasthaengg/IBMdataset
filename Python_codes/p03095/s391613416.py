from collections import Counter
n = int(input())
s = Counter(input())
mod = 10 ** 9 + 7

x = 1
for v in s.values():
  x *= (v+1)
ans = x - 1
print(ans%mod)