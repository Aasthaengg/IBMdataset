def solve():
  S = input()
  ans = min(S.count('0'),S.count('1'))*2
  return ans
print(solve())