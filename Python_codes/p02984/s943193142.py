N=int(input())
A=list(map(int,input().split()))
B=[]
ans=0
for i in range(N-1,-1,-1):
  if i%2==0:
    ans=A[i]-ans
  else:
    ans=A[i]-ans
B.append(ans)
for i in range(N-1):
  B.append(A[i]*2-ans)
  ans=A[i]*2-ans
print(*B)