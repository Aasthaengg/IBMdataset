a = input().rstrip().split(" ")
distance = int(a[0])
deadline = int(a[1])
speed = int(a[2])
if distance / speed > deadline:
  print("No")
else:
  print("Yes")