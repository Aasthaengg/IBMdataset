C = [list(map(int, input().split())) for i in range(3)]
for i in range(3):
  C[i] = [C[i][0]-min(C[i]), C[i][1]-min(C[i]), C[i][2]-min(C[i])]
for j in range(3):
  tmp = min(C[0][j], C[1][j], C[2][j])
  C[0][j] = C[0][j] - tmp
  C[1][j] = C[1][j] - tmp
  C[2][j] = C[2][j] - tmp
if C == [[0] *3 for i in range(3)]: print("Yes")
else: print("No")