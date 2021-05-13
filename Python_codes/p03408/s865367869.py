from collections import defaultdict

n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]

d=defaultdict(int)
for x in s:
  d[x]+=1
for y in t:
  d[y]-=1

print(max(0,max(d.values())))