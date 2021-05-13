W, H, x, ｙ = map(int, input().split())

w = W / 2
h = H / 2

if w == x and h == y:
  print(W*H/2, 1)
else:
  print(W*H/2, 0)