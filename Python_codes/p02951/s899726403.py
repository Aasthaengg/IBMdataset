S = list(map(int, input().split()))
ans = S[2] - (S[0] - S[1])
if ans < 0:
  print(0)
else:
  print(ans)