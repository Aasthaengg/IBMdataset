n=int(input())
a=list(map(int,input().split()))
A=[]
B=[]
for i in range (n):
  p=abs(a[i])
  A.append(p)
  if a[i]<0:
    B.append(a[i])
if len(B)%2==0:
  print(sum(A))
else:
  print(sum(A)-(min(A)*2),)
