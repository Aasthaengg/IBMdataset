n=int(input())
A=list(map(int,input().split()))
mod=10**9+7
B=[0]*n
for i in range(n):
  B[A[i]]+=1
a=0
if B[0]==1:
  for i in range(1,n):
    if i%2==0:
      if B[i]!=2:
        a=1
    else:
      if B[i]!=0:
        a=1
  if a==0:
    print(pow(2,(n-1)//2,mod))
  else:
    print(0)
elif B[0]==0:
  for i in range(1,n):
    if i%2==0:
      if B[i]!=0:
        a=1
    else:
      if B[i]!=2:
        a=1
  if a==0:
    print(pow(2,n//2,mod))
  else:
    print(0)
else:
  print(0)