n,k=map(int,input().split())
A=list(map(int,input().split()))

R=[0]*(n+1)
for i in range(1,n+1):
  R[i]=R[i-1]+A[i-1]

for i in range(1,n-k+1):
  if R[k+i]-R[i]>R[k+i-1]-R[i-1]:
    print('Yes')
  else:
    print('No')