n = int(input())
As = map(int, input().split())
from collections import defaultdict
dic = defaultdict(int)
for a in As:
  dic[a] += 1


table = [0] * (10**6+5)
for a, v in dic.items():
  for i in range(a, 10**6+5, a):
    table[i] += 1
ans = 0
for k, v in dic.items():
  if table[k] >= 2 and v == 1:
    ans += 1
  elif v >= 2:
    ans += v
print(n-ans)
