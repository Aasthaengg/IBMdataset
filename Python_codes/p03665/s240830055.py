N,P=map(int,input().split())
A=list(map(int,input().split()))
f=0
for i in range(N):
  if A[i]%2==1:
    f=1
if f==0:
  if P==0:
    print(2**N)
  else:
    print(0)
else:
  print(2**(N-1))