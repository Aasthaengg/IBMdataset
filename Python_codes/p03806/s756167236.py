N,Ma,Mb = map(int,input().split())

sz = 401
table = [[99999999]*(sz+1) for _ in range(sz+1)]
table[0][0] = 0
for n in range(N):
  a,b,c = map(int,input().split())
  for i in range(sz,-1,-1):
    for j in range(sz,-1,-1):
      if table[i][j]!=99999999:
        table[i+a][j+b] = min(table[i+a][j+b],table[i][j]+c)
#print(table)

ans = 99999999
i,j = Ma,Mb
while i<=sz and j<=sz:
  ans = min(ans,table[i][j])
  i += Ma
  j += Mb
print(ans if ans!=99999999 else -1)
