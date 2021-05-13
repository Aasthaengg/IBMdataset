def solve():
  ans = 0
  S = input()
  N = len(S)
  ans = [1]*N
  for i in range(N-1):
    if S[i]=='R':
      if S[i+1]=='R':
        ans[i+2] += ans[i]
        ans[i] = 0
  for i in range(N-1,0,-1):
    if S[i]=='L':
      if S[i-1]=='L':
        ans[i-2] += ans[i]
        ans[i] = 0
  return ans
print(*solve())