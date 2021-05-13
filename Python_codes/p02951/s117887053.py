A, B, C = map(int, input().split())
a = A - B
ans = C - a
if ans < 0:
  ans = 0
print(ans)