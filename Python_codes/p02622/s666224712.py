def solve():
  ans = 0
  S = input()
  T = input()
  for i in range(len(S)):
    if S[i]!=T[i]:
      ans += 1
  return ans
print(solve())