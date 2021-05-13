def MAP(): return map(int, input().split())
x = sorted(MAP())
if x[0] + x[1] == x[2]:
  print("Yes")
else:
  print("No")