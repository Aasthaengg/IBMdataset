(R,C,K),*t=[map(int,t.split())for t in open(0)]
G,*F=eval("eval('[0]*-~C,'*R),"*5)
for r,c,v in t:G[r-1][c]=v
for r in range(R):
 for x in 1,2,3:
  for c in range(C):F[x][r][c]=max(F[x-1][r][c],max(F[x-1][r][c-1],(x<2)*F[3][r-1][c])+G[r][c+1],F[x][r][c-1])
print(F[3][-1][-2])