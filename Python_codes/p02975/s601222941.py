n = int(input())
l = list(map(int, input().split()))
u = list(set(l))
if len(u)==1 and u[0]==0:
  print("Yes")
elif n%3==0:
  if len(u)==2:
    x = l.count(u[0])
    y = l.count(u[1])
    if (x==2*n/3 and y==n/3 and u[1]==0) or (y==2*n/3 and x==n/3 and u[0]==0):
      print("Yes")
    else:
      print("No")
  elif len(u)==3:
    x = l.count(u[0])
    y = l.count(u[1])
    z = l.count(u[2])
    if x==n/3 and y==n/3 and z==n/3 and ((u[0]^u[1])^u[2])==0:
      print("Yes")
    else:
      print("No")
  else:
    print("No")
else:
  print("No")

