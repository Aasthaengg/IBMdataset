N, M = map(int, input().split())
x=[0]*N
y=[0]*N
c=[0]*M
d=[0]*M
ans=[0]*N
for i in range(N):
  x[i],y[i]=map(int,input().split())
for i in range(M):
  c[i],d[i]=map(int, input().split())

for i in range(N):
  dmin=10**9
  for j in range(M):
    dcurr=abs(x[i]-c[j])+abs(y[i]-d[j])
    if dcurr<dmin:
      ans[i]=j+1
      dmin=dcurr

for n in ans:
  print(n)