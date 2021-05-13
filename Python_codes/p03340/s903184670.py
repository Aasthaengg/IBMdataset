N=int(input())
A=list(map(int,input().split()))
c=0
t=0
l=0
for r in range(N):
  if t+A[r]==t^A[r]:
    t+=A[r]
  else:
    while t+A[r]!=t^A[r]:
      t-=A[l]
      c+=r-l
      l+=1
    t+=A[r]
c+=(N-l)*(N-l+1)//2
print(c)