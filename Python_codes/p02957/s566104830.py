a,b=[int(x) for x in input().split()]

if(a+b)%2!=0:
  print("IMPOSSIBLE")
else:
  print((a+b)//2)