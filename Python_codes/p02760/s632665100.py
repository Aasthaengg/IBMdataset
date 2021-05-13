list = [list(map(int,input().split())) for i in range(3)]
N = int(input())
A = [[0] * 3 for i in range(3)]
for i in range(N):
  B = int(input())
  for j in range(3):
    for k in range(3):
      if list[j][k] == B:
        A[j][k] += 1
        
result = A[0][0] * A[0][1] * A[0][2]
result += A[1][0] * A[1][1] * A[1][2]
result += A[2][0] * A[2][1] * A[2][2]
result += A[0][0] * A[1][0] * A[2][0]
result += A[0][1] * A[1][1] * A[2][1]
result += A[0][2] * A[1][2] * A[2][2]
result += A[0][0] * A[1][1] * A[2][2]
result += A[0][2] * A[1][1] * A[2][0]
if result >= 1:
  print('Yes')
else:
  print('No')