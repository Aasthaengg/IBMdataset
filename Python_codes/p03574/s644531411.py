H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
dydx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def check(h, w):
  count = 0
  for dy, dx in dydx:
    if 0 <= h + dy < H and 0 <= w + dx < W and S[h+dy][w+dx] == '#':
      count += 1
  return count

for h in range(H):
  for w in range(W):
    if S[h][w] == '.':
      S[h][w] = str(check(h, w))
  res = "".join(S[h])
  print(res)