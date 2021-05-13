def solve():
  A, B, C = map(int, input().split())
  K = int(input())
  ans = A+B+C+max([A,B,C])*(pow(2,K)-1)
  return ans
print(solve())