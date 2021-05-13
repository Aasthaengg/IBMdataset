N = int(input())
S = [input() for _ in range(N)]
ans = 0
ba, __a, b__ = 0, 0, 0
for i in range(N):
  ans += S[i].count("AB")
  if S[i][0] != "B" and S[i][-1] == "A":
    __a += 1
  elif S[i][0] == "B" and S[i][-1] == "A":
    ba += 1
  elif S[i][0] == "B" and S[i][-1] != "A":
    b__ += 1
if ba > 0:
  ans += ba - 1
  if __a > 0:
    ans += 1
    __a -= 1
  if b__ > 0:
    ans += 1
    b__ -= 1
ans += min(b__, __a)
print(ans)