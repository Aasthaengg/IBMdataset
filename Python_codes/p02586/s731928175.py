R=3002
f=range(1,R)
G,*F=eval("eval('[0]*R,'*R),"*5)
for t in[*open(0)][1:]:r,c,v=map(int,t.split());G[r][c]=v
for r in f:
 for x in 1,2,3:
  for c in f:F[x][r][c]=max(F[x-1][r][c],max(F[x-1][r][c-1],(x<2)*F[3][r-1][c])+G[r][c],F[x][r][c-1])
print(F[3][-1][-1])