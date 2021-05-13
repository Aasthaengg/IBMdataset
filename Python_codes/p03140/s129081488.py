N=int(input())
A=input()
B=input()
C=input()

ans=0
for i in range(N):
  t=0
  if A[i]!=B[i]:
    t+=1
  if C[i]!=A[i] and C[i]!=B[i]:
    t+=1
  ans+=t
print(ans)