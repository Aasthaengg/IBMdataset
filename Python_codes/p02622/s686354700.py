S = list(input())
T = list(input())
ans = 0
for k in range(len(S)):
  if S[k] != T[k]:
    ans += 1
print(ans)