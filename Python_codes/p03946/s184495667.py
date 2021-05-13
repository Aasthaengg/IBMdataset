N,T=map(int,input().split())
A=tuple(map(int,input().split()))
x=[0]*N
x[0]=A[0]
for i in range(1,N):
  x[i]=min(x[i-1],A[i])
B={}
for i in range(1,N):
  tmp=A[i]-x[i-1]
  if tmp<0:
    continue
  if tmp not in B:
    B[tmp]=1
  else:
    B[tmp]+=1
d=list(B.items())
d.sort(reverse=True)
print(d[0][1])