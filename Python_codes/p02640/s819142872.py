input_line = input().split(" ")
X = int(input_line[0])
Y = int(input_line[1])
Pat = 0
for i in range(X + 1):
  C = i
  T = X - i
  Cf = C * 2
  Tf = T * 4
  F = Cf + Tf
  if Y == F:
      Pat = Pat + 1
if Pat > 0:
  print("Yes")
else:
  print("No")
