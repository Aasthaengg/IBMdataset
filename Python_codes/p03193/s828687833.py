N,H,W = map(int, input().split())
R = 0
for x in range(N):
  h,w = map(int, input().split())
  if h >= H and w >= W:
    R += 1
print(R)