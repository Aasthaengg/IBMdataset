N = int(input())
S = input()
B = 0
R = 0
for s in S:
  if s == "B":
    B += 1
  else:
    R += 1
if R > B:
  print("Yes")
else:
  print("No")