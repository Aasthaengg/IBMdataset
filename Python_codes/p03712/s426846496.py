H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]
ans = ""
for i in range(H+2):
  for j in range(W+2):
    if 1 <= i <= H and 1 <= j <= W:
      ans += a[i-1][j-1]
    else:
      ans += '#'
  ans += "\n"
print(ans)