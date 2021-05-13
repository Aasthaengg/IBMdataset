H, W  = map(int, input().split())
X = [list(input().split()) for i in range(H)]
for i in range(2*H):
  print(*X[int(i/2)])