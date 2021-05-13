IN = list(map(int, input().split()))
if max([abs(IN[0]-IN[1]), abs(IN[2]-IN[1])]) <= IN[3] or abs(IN[0]-IN[2]) <= IN[3]:
  print("Yes")
else:
  print("No")
