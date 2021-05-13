h,w=map(lambda x:range(int(x)),input().split())
g=[[c=='.'for c in input()]for _ in h]
a=[[-3]*len(w)for _ in h]
for i in h:
  l=r=0
  for j in w: l=-~l*g[i][j]; a[i][j]+=l; r=-~r*g[i][~j]; a[i][~j]+=r
for i in w:
  d=u=0
  for j in h: d=-~d*g[j][i]; a[j][i]+=d; u=-~u*g[~j][i]; a[~j][i]+=u
print(max(a[i][j] for i in h for j in w))