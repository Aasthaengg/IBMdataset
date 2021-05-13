from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
  d[ai] += 1
  
ans = 0
for key in d:
  if d[key] >= key:
    ans += (d[key] - key)
  else:
    ans += d[key]
print(ans)