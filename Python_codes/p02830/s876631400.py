def solve():
  N = int(input())
  S,T = input().split()
  ans = ''.join([s+t for s,t in zip(S,T)])
  return ans
print(solve())