H, W = map(int, input().split())
A = [input() for _ in range(H)]

def check(n4, n2):

  for i in range(27):
    if n4 == 0:
      break
    while alpha[i] >= 4:
      alpha[i] -= 4
      n4 -= 1
      if n4 == 0:
        break

  for i in range(27):
    if n2 == 0:
      break
    while alpha[i] >= 2:
      alpha[i] -= 2
      n2 -= 1
      if n2 == 0:
        break
      
  if n4 == 0 and n2 == 0:
    print("Yes")
  else:
    print("No")      

alpha = [0] * 27
for i in range(H):
  for j in range(W):
    alpha[ord(A[i][j]) - ord("a")] += 1

if H % 2 and W % 2:
  n4 = (H * W - (H + W) + 1) // 4
  n2 = (H + W - 2) // 2
elif H % 2 == 0 and W % 2 == 0:
  n4 = H * W // 4
  n2 = 0
else:
  if H % 2:
    H, W = W, H
  n4 = (W - 1) * H // 4
  n2 = H // 2
check(n4, n2)