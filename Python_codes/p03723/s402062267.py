A, B, C = map(int, input().split())
if A == B == C:
  if A % 2 == 0:
    print(-1)
  else:
    print(0)
else:
  ans = 0
  while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    p, q, r = A // 2, B // 2, C // 2
    A, B, C = q + r, p + r, p + q
    ans += 1
  print(ans)