N = int(input())
S = list(str(input()))
WH = S.count(".")
ans = WH
for i in range(N):
  if S[i] == "#":
    WH += 1
  else:
    WH -= 1
  ans = min(ans, WH)

print(ans)