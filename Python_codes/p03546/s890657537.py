from collections import defaultdict
import sys

h,w=map(int,input().split())
costs=[]
for _ in range(10):
  costs.append(list(map(int,input().split())))
dd=defaultdict(lambda:0)
for i in map(int,sys.stdin.read().split()):
  dd[i]+=1
  
min_costs=[0]*10
for y in range(10):
  min_costs[y]=costs[y][1]

for _ in range(100):
  for x in range(10):
    for y in range(10):
      min_costs[y]=min(min_costs[y], min_costs[x]+costs[y][x])

ans=0
for i in range(10):
  ans+=dd[i]*min_costs[i]
print(ans)
