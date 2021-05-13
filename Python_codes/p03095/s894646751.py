from collections import Counter

MOD = 10**9+7

N = int(input())
s = input()
d = Counter(s)
res = 1
for value in d.values():
  res *= value + 1
  res %= MOD
res -= 1
print(res)