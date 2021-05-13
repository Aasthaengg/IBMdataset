INPUT = list(input().split())
H = int(INPUT[0])
A = int(INPUT[1])
if H%A == 0:
  print(H//A)
else:
  print(H//A + 1)