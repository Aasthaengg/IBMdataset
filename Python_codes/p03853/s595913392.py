H, W = map(int, input().split())
a = []
for i in range(H):
  b = list(input())
  a.append(b)
for i in range(2*H):
  for j in range(W):
    if j != W - 1:
      print(a[i//2][j],end="")
    else:
      print(a[i//2][j])