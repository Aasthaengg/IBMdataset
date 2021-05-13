N,k=map(int,input().split())
A=input()
ans=0
for i in range(0,N):
  if A[i]=='R' and i<N-1:
    if A[i+1]=='R':
      ans=ans+1
  if A[i]=='L' and i>0:
    if A[i-1]=='L':
      ans=ans+1
print(min(N-1,2*k+ans))

