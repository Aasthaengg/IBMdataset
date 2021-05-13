H, W, A, B = map(int, input().split())

for i in range(H):
  for j in range(W):
    if i < B and j < A or i >= B and j >= A:
      print(0, end="")
    else:
      print(1, end="")
  print("")