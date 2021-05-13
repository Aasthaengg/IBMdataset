f=lambda:[*map(int,input().split())]
H,W=f()
r=range(10)
c=[f() for _ in r]
C=[0]*10

for _ in range(H):
  for i in f():
    if i>=0:
      C[i]+=1

for k in r:
  for i in r:
    for j in r:
      c[i][j]=min(c[i][j],c[i][k]+c[k][j])

print(sum(c[i][1]*C[i] for i in r))