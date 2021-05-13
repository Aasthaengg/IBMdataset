N = int(input())
S = [int(input()) for _ in range(N)]

S.sort()
ans = sum(S)
if ans%10 != 0:
  print(ans)
else:
  for i in range(N):
    if S[i]%10 != 0:
      ans -= S[i]
      break
  if ans == sum(S):
    ans = 0
  print(ans)