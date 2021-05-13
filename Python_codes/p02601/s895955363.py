a,b,c=map(int,input().split())
k=int(input())
while k>0:
  if not b>a:
    b*=2
    k-=1
  elif not c>b:
    c*=2
    k-=1
  else:
    break

if c>b and b>a:
  print("Yes")
else:
  print("No")
