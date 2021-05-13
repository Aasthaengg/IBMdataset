H, W, K  = map(int, input().split())
MOD = 10**9+7



L = [0]*(W-1)
row = 0
for i in range(2**(W-1)):
  LL = format(i, '08b')
  Lf = 0
  for j in range(len(LL)-1):
    if LL[j] == "1" and LL[j+1] == "1":
      Lf = 1
  if Lf == 0:
    row += 1
    LL = LL[8-(W-1):]
    for k in range(W-1):
      if LL[k] == "1":
        L[k] += 1
  #print(LL,Lf)
    


B = [] #Bridge
for _ in range(W):
  B.append([0,0,0])

for i in range(W):
  if i != 0:
    B[i][0] = L[i-1]
  else:
    B[i][0] = 0
  
  if i != W-1:
    B[i][2] = L[i]
  else:
    B[i][2] = 0

  B[i][1] = row-B[i][0]-B[i][2] 


A = [[0]*(W+2)]
for _ in range(H):
  A.append([0]*(W+2))

A[0][1] = 1

for i in range(H):
  for j in range(1,W+1):
    A[i+1][j-1] += A[i][j] * (B[j-1][0])
    A[i+1][j] += A[i][j] * (B[j-1][1])
    A[i+1][j+1] += A[i][j] * (B[j-1][2])

print(A[H][K]%MOD)