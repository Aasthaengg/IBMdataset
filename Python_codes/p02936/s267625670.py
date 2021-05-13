import sys
sys.setrecursionlimit(1000000)
n,q=map(int,input().split())

d=[[0] for _ in range(n+1)]
d1=[0 for _ in range(n+1)]

for i in range(n-1):
  a,b=map(int,input().split())
  d[a].append(b)
  d[b].append(a)

for i in range(q):
  p,x=map(int,input().split())
  d1[p]+=x

#d 関係性 d1価
vi=[-1 for _ in range(n+1)]

def dfs(x,i):
  vi[x]=i+d1[x]
  for m in d[x]:
    if vi[m]==-1 and m!=0:
      dfs(m,vi[x])    

dfs(1,0)


print(*vi[1:])