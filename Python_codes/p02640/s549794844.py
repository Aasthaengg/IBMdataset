x,y = map(int, input().split())
if y-2*x >= 0 and (y-2*x)%2 == 0 and (y-2*x)//2 <= x:
  print("Yes")
else:
  print("No")