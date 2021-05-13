def solve():
  S = input()
  ans = 0
  now = ''
  i = 0
  while i<len(S)-1:
    if S[i]==now:
      now += S[i+1]
      i += 1
    else:
      now = S[i]
    i += 1
    ans += 1
  if i==len(S)-1 and now!=S[i]:
    ans += 1
  return ans
print(solve())