A = []
for _ in range(3):
  A.append(list(map(int, input().split())))

B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
N =int(input())
for _ in range(N):
  b = int(input())
  for k in range(3):
    for j in range(3):
      if A[k][j] == b:
        B[k][j] = 1

if sum(B[0]) == 3 or sum(B[1]) == 3 or sum(B[2]) == 3:
  print('Yes')
elif B[0][0] + B[1][0] + B[2][0] ==3:
  print('Yes')
elif B[0][1] + B[1][1] + B[2][1] ==3:
  print('Yes')
elif B[0][2] + B[1][2] + B[2][2] ==3:
  print('Yes')
elif B[0][0] + B[1][1] + B[2][2] ==3:
  print('Yes')
elif B[0][2] + B[1][1] + B[2][0] ==3:
  print('Yes')
else:
  print('No')