A=list(map(int,input().split()))
A.sort()
a=A[2]-A[1]
b=A[2]-A[0]
if a%2==0 and b%2==0:
  print(a//2+b//2)
elif a%2==1 and b%2==1:
  print(a//2+b//2+1)
else:
  print(a//2+1+b//2+1)