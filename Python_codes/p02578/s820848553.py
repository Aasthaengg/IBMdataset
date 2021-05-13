n=int(input())

A = list(map(int, input().split()))
l = [0] * len(A)

ans=0

for i in range(n-1):
  if A[i]>=A[i+1]:
    l[i+1]=A[i]-A[i+1]
    A[i+1]=A[i]
  else:
    l[i+1]=0
  ans=ans+l[i+1]  
print(ans)  
