N=int(input())
A=input()
B=input()
C=input()

ans=0
for i in range(N):
  if A[i]==B[i]==C[i]:
    ans=ans
  elif A[i]!=B[i]!=C[i]!=A[i]:
    ans=ans+2
  else:
    ans=ans+1

print(ans)