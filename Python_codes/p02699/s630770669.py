s, w = map(int, input().split())
ans = "safe"
if s <= w:
  ans = "un" + ans
print(ans)