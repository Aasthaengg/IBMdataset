from collections import defaultdict
mod = pow(10, 9) + 7
N = int(input())
S = input()
d = defaultdict(int)
for s in S:
  d[s] += 1
ans = 1
for c in d:
  ans *= (d[c] + 1)
  ans %= mod
print(ans - 1)