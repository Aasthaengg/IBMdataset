H, W, A, B = map(int, input().split())
ans = [["0" for _ in range(W)] for _ in range(H)]

for i in range(H):
  if i + 1 <= B:
    ans[i][A:] = ["1"] * (W-A)
  else:
    ans[i][:A] = ["1"] * A

for j in ans:
  print("".join(j))