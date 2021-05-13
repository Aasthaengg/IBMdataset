W, H, x, y = map(int, input().split())
ans = 0
c = 0
if x*2 == W and y*2 == H:
  ans = W*H/2
  c = 1
else:
  ans = W*H/2
  c = 0
print(ans,c)