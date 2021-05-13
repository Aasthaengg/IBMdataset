def solve():
  A, B, C = map(int, input().split())
  ans = B+min(A+B+1,C)
  return ans
print(solve())