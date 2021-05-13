h,w=map(int,input().split())
f=range
g=[[c=='.'for c in input()]for _ in f(h)]
a=[[-3]*w for _ in f(h)]
for i in f(h):
  l=r=0
  for j in f(w): l=-~l*g[i][j]; a[i][j]+=l; r=-~r*g[i][~j]; a[i][~j]+=r
for i in f(w):
  d=u=0
  for j in f(h): d=-~d*g[j][i]; a[j][i]+=d; u=-~u*g[~j][i]; a[~j][i]+=u
print(max(a[i][j] for i in f(h) for j in f(w)))