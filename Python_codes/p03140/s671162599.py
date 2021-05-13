N=int(input())
A=input()
B=input()
C=input()
ans=0
if A==B==C:
  ans=0
else:
  for i in range(N):
    x=[A[i],B[i],C[i]]
    ans+=len(list(set(x)))-1
print(ans)
