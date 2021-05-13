d, t, s = list(map(int, input().split(" ")))
 
min = d / s
 
if min <= t:
  print("Yes")
else:
  print("No")