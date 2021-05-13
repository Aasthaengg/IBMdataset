def solve():
  N = int(input())
  V = list(map(int, input().split()))
  V.sort(reverse=True)
  for _ in range(N-1):
    V[-2] = (V[-1]+V[-2])/2
    V.pop(-1)
  ans = V[0]
  return ans
print(solve())