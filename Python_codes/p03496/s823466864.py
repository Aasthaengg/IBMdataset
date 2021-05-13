n=int(input())
a=list(map(int,input().split()))
A=[]
for i in range(n):
  A.append(abs(a[i]))
m=A.index(max(A))
print(2*n-1)
for i in range(1,n+1):
  print(m+1,i)
if a[m]>=0:
  for i in range(1,n):
    print(i,i+1)
else:
  for i in range(n,1,-1):
    print(i,i-1)