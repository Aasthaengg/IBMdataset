h,w=map(int,input().split())
f=lambda:[[0]*w for _ in range(h)]
g=[input() for _ in range(h)]
l,r=f(),f()
for i in range(h):
  lc=rc=0
  for j in range(w):
    if g[i][j]=='.': lc+=1; l[i][j]=lc
    else: lc=0
    if g[i][-1-j]=='.': rc+=1; r[i][-1-j]=rc
    else: rc=0
d,u=f(),f()
for i in range(w):
  dc=uc=0
  for j in range(h):
    if g[j][i]=='.': dc+=1; d[j][i]=dc
    else: dc=0
    if g[-1-j][i]=='.': uc+=1; u[-1-j][i]=uc
    else: uc=0
print(max(l[i][j]+r[i][j]+d[i][j]+u[i][j]-3 for i in range(h) for j in range(w)))