a,b,c=map(int,input().split())
s=a+b+c
if s%2==1:
  print("No")
  exit()
n=s//2
if n in [a,b,c]:
  print("Yes")
else:
  print("No")