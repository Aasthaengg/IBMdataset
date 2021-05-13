num = int(input())
cap = list(input())
red = 0
blue = 0
for c in cap:
  if c == 'B':
    blue += 1
  else:
    red += 1
if red > blue:
  print("Yes")
else:
  print("No")
