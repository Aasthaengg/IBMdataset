n = list(map(int,input().split()))
ans = n[0] + n[1] - n[2] - n[3]
if ans > 0:
  print("Left")
elif ans == 0:
  print("Balanced")
else:
  print("Right")