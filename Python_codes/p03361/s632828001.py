H, W = list(map(lambda n: int(n), input().split(" ")))
S = []
for i in range(H):
  if i == 0:
    S.append("X" * (W + 2))
  S.append("X" + input() + "X")
else:
  S.append("X" * (W + 2))

unpaintable = False
for i in range(1, H+1):
  for j in range(1, W+1):
    if S[i][j] == "#" and "#" not in [S[i-1][j], S[i+1][j], S[i][j-1], S[i][j+1]]:
      unpaintable = True
      break
      
print("No") if unpaintable else print("Yes")