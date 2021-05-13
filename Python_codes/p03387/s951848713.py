A, B, C = map(int, input().split())
M = max(A, B, C)
s = 3 * M - A - B - C
if s % 2 == 0:
  ans = s // 2
else:
  ans = (s + 3) // 2
print(ans)