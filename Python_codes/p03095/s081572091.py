from collections import Counter
N = int(input())
S = str(input())

c = Counter(S)
l = list(c.values())

ans = 1
for n in l:
  ans *= n+1
ans %= (10**9+7)
print(ans-1)