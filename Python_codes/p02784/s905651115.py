a,b=input().split()
a=int(a)
b=int(b)
c=list(map(int,input().split()))
if sum(c)>=a:
  print("Yes")
else:
  print("No")