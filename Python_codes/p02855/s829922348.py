H,W,K = list(map(int, input().split()))
S = []
for i in range(H):
  S.append(input())
  
A = [[0 for i in range(W)] for j in range(H)]

pt = 1
for i in range(H):
  if S[i][:] == "." * W:
    if i > 0:
      A[i][:] = A[i-1][:]
      continue
      
  firstFlg = True
  for j in range(W):
    if firstFlg and S[i][j] == "#":
      for k in range(0,j+1):
        A[i][k] = pt
      pt += 1
      firstFlg = False
    elif S[i][j] == "#":
      A[i][j] = pt
      pt += 1
    else:
      A[i][j] = pt-1

for i in range(H-1,-1,-1):
  if A[i] == [0 for j in range(W)]:
    A[i][:] = A[i+1][:]

for i in range(H):
  print(" ".join(list(map(str,A[i]))))