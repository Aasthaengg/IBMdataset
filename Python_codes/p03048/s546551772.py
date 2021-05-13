R, G, B, N = map(int, input().split())
ans = 0
r = 0
while r <= N:
  g = 0
  while r + g <= N:
    if (N - r - g) % B == 0:
      ans += 1
    g += G
  r += R
print(ans)