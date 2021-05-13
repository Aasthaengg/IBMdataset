R, G, B, N = map(int, input().split())
r = N // R + 2
g = N // G + 2
ans = 0
for x in range(r):
  for y in range(g):
    Bz = N - R * x - G * y
    if Bz >= 0 and Bz % B == 0:
      ans += 1
    elif Bz < 0:
      break
print(ans)