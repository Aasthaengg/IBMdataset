n=int(input())
D=[0]*(n+1)
F=[0]*(n+1)
v=[[] for i in range(n+1)]
flg=True
t=1
for i in range(n):
  a=list(map(int,input().split()))
  v[a[0]]=sorted(a[2:])

def dfs(p):
  global t
  if D[p]!=0: return
  D[p]=t
  t+=1
  for i in v[p]:
    if D[i]==0: dfs(i)
  F[p]=t
  t+=1

while flg:
  flg=False
  for i in range(1,n+1):
    if D[i]==0:
      flg=True
      dfs(i)

for i in range(1,n+1):
  print(f'{i} {D[i]} {F[i]}')
