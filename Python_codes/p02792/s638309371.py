L = [[0]*10 for _ in range(10)]
S = 0
for i in range(1, int(input())+1):
  L[int(str(i)[0])][int(str(i)[-1])] += 1
for j in range(9):
  for i in range(j+1, 10):
    S += 2*L[j][i]*L[i][j]
for i in range(10):
  S += L[i][i]**2
print(S)