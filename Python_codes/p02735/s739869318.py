H,W = list(map(int, input().split()))
B = []
for _ in range(H):
  B.append(input())
  
A = [[999999 for _ in range(W)] for _ in range(H)]
A[0][0] = 0 if B[0][0] == "." else 1

for i in range(H):
  for j in range(W):
    if i+j == 0:
      continue
    X,Y = 999999, 999999
    if i > 0:
      X = A[i-1][j] 
      X += 1 if B[i-1][j] == '.' and B[i][j] == '#' else 0
    if j > 0:
      Y = A[i][j-1]
      Y += 1 if B[i][j-1] == '.' and B[i][j] == '#' else 0
    A[i][j] = min(X,Y)
    
print(A[H-1][W-1])
#for i in range(H):
#  print(A[i])