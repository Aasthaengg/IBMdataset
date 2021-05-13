l = [int(x) for x in input().split(' ')]
if l[0] + l[1] < l[2] + l[3]:
  print("Right")
elif l[0] + l[1] > l[2] + l[3]:
  print("Left")
else:
  print("Balanced")