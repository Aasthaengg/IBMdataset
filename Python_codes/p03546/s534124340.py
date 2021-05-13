f=lambda:[*map(int,input().split())]
h,w=f()
r=range(10)
c=[f() for _ in r]
C=[0]*10
for _ in range(h):
  for i in f():
    if i>=0: C[i]+=1
m=[c[i][1] for i in r]
for _ in r:
  for i in r:
    for j in r:
      m[i]=min(m[i],c[i][j]+m[j])
print(sum(m[i]*C[i] for i in r))