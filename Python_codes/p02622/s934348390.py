S = input()
T = input()
if S == T:
  print(0)
  exit(0)
ans = 0
for i in range(len(S)):
  if S[i] != T[i]:
    ans += 1
print(ans)