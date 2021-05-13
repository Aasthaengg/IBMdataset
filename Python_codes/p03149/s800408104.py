N = [int(i) for i in input().split()]
n1,n2,n3,n4=0,0,0,0
for n in N:
  if n == 1:
    n1 = 1
  elif n == 9:
    n2 = 1
  elif n == 7:
    n3 = 1
  elif n == 4:
    n4 = 1
if n1==n2==n3==n4==1:
  print("YES")
else:
  print("NO")