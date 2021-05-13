N = int(input())
S = input()
import collections

c = collections.Counter(S)

ls = list(c.values())

ans = 1
for l in ls:
  ans *= (l+1)

print((ans-1)%(10**9+7))
