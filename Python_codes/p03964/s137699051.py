N=int(input())
T=[]
A=[]
for i in range(N):
  t,a=map(int,input().split())
  T.append(t)
  A.append(a)
a=1
b=1
for i in range(N):
  n=max((a+T[i]-1)//T[i], (b+A[i]-1)//A[i])
  a=n*T[i]
  b=n*A[i]
print(a+b)
