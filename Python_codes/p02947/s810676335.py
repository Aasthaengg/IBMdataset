from collections import defaultdict
n = int(input())
d = defaultdict(int)
sens = set()
ans = 0
for _ in range(n):
  s = sorted(input())
  s = ''.join(s)
  if s in sens:
    d[s] += 1
    ans += d[s]
  else:
    sens.add(s)
print(ans)