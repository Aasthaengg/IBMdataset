n,m,p=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
I=float('inf')
d=[0]*2+[I]*n
for i in range(n-1):
  for a,b,c in l:
    d[b]=min(d[b],d[a]-c+p)
x=d[n]
for i in range(n):
  for a,b,c in l:
    if d[b]>d[a]-c+p:d[b]=-I
print([max(-d[n],0),-1][d[n]!=x])