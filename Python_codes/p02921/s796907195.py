S = input()
T = input()

ans = 0
for i in [0, 1, 2]:
  if S[i] == T[i]:
    ans = ans + 1
print(ans)