C = [list(map(int, input().split())) for i in range(3)]
A = []
B = []
for i in range(3):
  A.append([C[0][i] - C[1][i], C[1][i] - C[2][i], C[2][i] - C[0][i]])
for i in range(3):
  B.append([C[i][0] - C[i][1], C[i][1] - C[i][2], C[i][2] - C[i][0]])
ans = 'Yes'
if A[0] != A[1]:
  ans = 'No'
elif A[1] != A[2]:
  ans = 'No'
elif B[0] != B[1]:
  ans = 'No'
elif B[1] != B[2]:
  ans = 'No'
print(ans)