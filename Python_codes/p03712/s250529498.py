H,W = map(int,input().split())
A = [list(input()) for _ in range(H)]

ANS = []
for i in range(H+2):
  t = []
  for j in range(W+2):
    if i == 0 or j == 0 or i == H+1 or j == W+1:
      t.append("#")
    else:
      t.append(A[i-1][j-1])
  ANS.append("".join(t))
  
print("\n".join(ANS))
