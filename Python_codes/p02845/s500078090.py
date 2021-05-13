n=int(input())
A=list(map(int,input().split()))
B=[0]*3
ans=1
for i in range(n):
  a=0
  for j in range(3):
    if A[i]==B[j]:
      a=a+1
  ans=ans*a
  for j in range(3):
    if A[i]==B[j]:
      B[j]=B[j]+1
      break
print(ans%(10**9+7))