list = list(map(int, input().split()))
s = list[0]
w = list[1]
if s<=w:
  print("unsafe")
else:
  print("safe")