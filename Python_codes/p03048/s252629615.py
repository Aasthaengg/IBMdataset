def solve():
  ans = 0
  R, G, B, N = map(int, input().split())
  for r in range(N//R+1):
    for g in range(N//G+1):
      bb = N-r*R-g*G
      if bb>=0 and bb%B==0:
        ans += 1
  return ans
print(solve())