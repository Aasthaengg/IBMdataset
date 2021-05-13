n=int(input())
A=[1,1]
for i in range(n):
  t,a=map(int,input().split())
  tt=(A[0]+t-1)//t
  aa=(A[1]+a-1)//a
  A[0]=max(tt,aa)*t
  A[1]=max(tt,aa)*a
print(A[0]+A[1])