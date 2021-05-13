A, B, C = map(int, input().split())

ans = 0
if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
  ans = min(A * B, min(A * C, B * C))
else:
  ans = 0

print(ans)
