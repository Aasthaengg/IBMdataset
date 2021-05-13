S = input()
T = input()
N = len(S)
ans = "No"
for i in range(N):
  if S == T:
    ans = "Yes"
    break
  S = S[1:] + S[0]
print(ans)