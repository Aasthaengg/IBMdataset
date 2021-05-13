def solve():
  H = int(input())
  W = int(input())
  N = int(input())
  ans = -(-N//max(H,W))
  return ans
print(solve())