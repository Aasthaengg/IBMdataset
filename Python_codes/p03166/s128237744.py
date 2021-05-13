import collections
import sys
sys.setrecursionlimit(10**9)
cache,edge={},collections.defaultdict(list)
def dp(node):
  if node in cache:
    return cache[node]
  lcl_max=0
  for child in edge[node]:
    
    lcl_max=max(lcl_max,1+dp(child))
  cache[node]=lcl_max
  return lcl_max
 
max_dis=0

n,m=map(int,input().split())
for _ in range(m):
  a,b=map(int,input().split())
  edge[a].append(b)
for node in range(1,n+1):
  max_dis=max(max_dis,dp(node))
print(max_dis)