def solve():
  S = input()
  a = S.find('A')
  z = S[::-1].find('Z')
  ans = len(S)-a-z
  return ans
print(solve())