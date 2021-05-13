H, W, N = map(int, input().split())
AB = dict()
for i in range(N):
  a, b = list(map(int, input().split()))
  for i in range(3):
    for j in range(3):
      x = (a - 1) - i
      y = (b - 1) - j
      if (0 <= x < H - 2) and (0 <= y < W - 2):
        ab = str(x) + "ab" + str(y)
        if ab in AB:
          AB[ab] += 1
        else:
          AB[ab] = 1
#print(AB)          

ans = [0] * 10
for i in AB.values():
  ans[i] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans)
for i in range(10):
  print(ans[i])