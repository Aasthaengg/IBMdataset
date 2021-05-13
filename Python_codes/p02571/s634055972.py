S = str(input())
T = str(input())
if T in S:
  print(0)
  exit()
ans, substr = 0, ""
for i in range(len(S) - len(T) + 1):
  substr = S[i: i + len(T)]
  cnt = 0
  for s, t in zip(substr, T):
    if s == t:
      cnt += 1
  ans = max(ans, cnt)
  if ans == len(T) - 1:
    break
print(len(T) - ans)