a,b=map(int,input().split())
c=b-a
if c%2==1:
  print("IMPOSSIBLE")
else:
  print(a+int(c/2))