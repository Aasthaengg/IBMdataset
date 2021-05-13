from collections import defaultdict

n,m=map(int,input().split())
r=[list(map(int,input().split())) for _ in range(m)]
d=defaultdict(int)
for x in r:
  d[x[0]]+=1
  d[x[1]]+=1

for i in range(1,n+1):
  print(d[i])
