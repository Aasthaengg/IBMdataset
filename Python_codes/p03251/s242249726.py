N, M, X, Y = list(map(int, input().split(" ")))

x_coord = list(map(int, input().split(" ")))
y_coord = list(map(int, input().split(" ")))

is_war = True

for Z in range(X, Y+1):
  if X < Z <= Y and max(x_coord) < Z and min(y_coord) >= Z:
    is_war = False
    break

if is_war:
  print("War")
else:
  print("No War")