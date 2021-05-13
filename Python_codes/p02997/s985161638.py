n,k=map(int,input().split())
if k>(n-1)*(n-2)//2:exit(print(-1))
edge=[n*[1]for _ in range(n)]
def ans():
  an=[]
  for i in range(n):
    for j in range(i+1,n):
      if edge[i][j]:an.append((i+1,j+1))
  print(len(an))
  for i in an:print(*i)
for i in range(n):edge[i][i]=0
for i in range(1,n):
  for j in range(i+1,n):
    if k==0:exit(ans())
    edge[i][j]=0
    k-=1
    if k==0:exit(ans())
if n==2:print(1);print(1,2)