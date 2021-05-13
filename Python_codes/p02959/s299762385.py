n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=sum(A)
for i in range(n):
  if B[i] > A[i]:
    A[i+1]=max(0,A[i+1]-(B[i]-A[i]))
    A[i]=0
  else:
    A[i]-=B[i]
    B[i]=0
print(ans-sum(A))