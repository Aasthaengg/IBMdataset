a,b = map(int,input().split())
k = (a+b)//2
if k-a==b-k:
  print(k)
else:
  print("IMPOSSIBLE")