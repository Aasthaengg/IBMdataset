W, a, b = map(int,input().split())
 
if (a+W)<=b:
  print(b-(a+W))
elif (a<= b)and (b<(a+W)):
  print(0)
elif ((a-W)<=b) and(b<a):
  print(0)
elif b<(a-W):
  print(a-(b+W))