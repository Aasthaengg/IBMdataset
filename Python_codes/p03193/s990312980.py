N, H, W = map(int, input().split())
c = 0
for i in range(N):
  H_, W_ = map(int, input().split())
  if H_ >= H and W_ >= W:
    c += 1
print(c)