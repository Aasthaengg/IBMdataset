N=int(input())
f=lambda:map(int,input().split())
*A,=f()
*B,=f()

cnt=0
for i in range(len(B)):
  a=min(A[i], B[i])
  cnt+=a
  a=min(A[i+1],B[i]-a)
  cnt+=a
  A[i+1]-=a
print(cnt)