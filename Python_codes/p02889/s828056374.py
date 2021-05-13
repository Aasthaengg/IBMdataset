n,m,l=map(int,input().split())
abc=[list(map(int,input().split())) for _ in range(m)]

"""
g=[[] for _ in range(n)]
for a,b,c in abc:
  if c>l:continue
  a,b=a-1,b-1
  g[a].append([b,c])
  g[b].append([a,c])
"""
q=int(input())
st=[list(map(int,input().split())) for _ in range(q)]

def warshall_floyd(d):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j] = min(d[i][j],d[i][k] + d[k][j])
  return d
inf=float('inf')
d=[[inf]*n for _ in range(n)]

for a,b,c in abc:
  a,b=a-1,b-1
  d[a][b]=c
  d[b][a]=c
for i in range(n):
  d[i][i]=0
d=warshall_floyd(d)
nabc=[]
dd=[[inf]*n for _ in range(n)]
#g=[[] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if d[i][j]<=l:
      dd[i][j]=1
for i in range(n):
  dd[i][i]=0
dd=warshall_floyd(dd)
for s,t in st:
  s,t=s-1,t-1
  tmp=dd[s][t]
  print(max(0,tmp-1) if tmp!=inf else -1)
#print(dd)