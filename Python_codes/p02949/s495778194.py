(n,m,p),*l=[list(map(int,s.split()))for s in open(0)];I=float('inf');d=[0]*2+[I]*n
for i in range(n*2):
 for a,b,c in l:
  if d[b]>d[a]-c+p:d[b]=[min(d[b],d[a]-c+p),-I][i>n]
 if i==n:x=d[n]
print([max(-d[n],0),-1][d[n]!=x])