from collections import Counter

n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]

c1 = Counter(s)
c2 = Counter(t)

MAX=0
for k1 in c1.keys():
  count = c1[k1]
  for k2 in c2.keys():
    if k1==k2:
      count -= c2[k2]
  MAX = max(MAX,count)

print(MAX)