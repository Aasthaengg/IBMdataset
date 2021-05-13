N,x=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
for i in range(len(A)):
  if x-A[i]<0:
    print(i)
    exit()
  else:
    x-=A[i]
if x==0:print(N)
else:print(N-1)

