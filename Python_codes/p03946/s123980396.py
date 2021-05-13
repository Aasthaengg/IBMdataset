n,t=map(int,input().split())
A=list(map(int,input().split()))
a=10**10
b=0
c=0
ans=0
for i in range(n):
  if A[i]<a:
    a=A[i]
    b=0
  if A[i]>b:
    b=A[i]
    if b-a>c:
      c=b-a
      ans=0
    elif b-a==c:
      ans=ans+1
print(ans+1)