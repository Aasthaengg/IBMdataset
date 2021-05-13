s = list(input())
s = list(map(int,s))
s = sum(s)
if s%9 == 0:
  print("Yes")
else:
  print("No")