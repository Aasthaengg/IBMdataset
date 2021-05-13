A, B, C, D, E, F = map(int, input().split())
A *= 100
B *= 100
dp = [[False]*(F+1) for i in range(F+1)]
dp[0][0] = True
for f in range(F+1):
  for s in range(F+1):
    if dp[f][s]:
      if f+C<=F and s+C<=F:
        dp[f+C][s+C] = True
      if f+D<=F and s+D<=F:
        dp[f+D][s+D] = True
      if f + A <= F:
        dp[f+A][s] = True
      if f + B <= F:
        dp[f+B][s] = True

ans = (float('inf'), 0)
for f in range(F+1):
  for s in range(F+1):
    if dp[f][s]:
      if s*100 <= E*(f-s):
        if ans[1]*f < ans[0]*s:
          ans = (f, s)

if ans[0] < float('inf'):
  print(*ans)
else:
  print(A, 0)