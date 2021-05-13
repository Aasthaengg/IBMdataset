a,b=map(int,input().split())
c=int((a+b)/2)
if (a+b)%2!=0:
  print("IMPOSSIBLE")
else:
  print(c)