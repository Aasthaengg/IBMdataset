d,t,s = [int(i) for i in input().split()]
if (d+s-1)//s <= t:
  print("Yes")
else:
  print("No")