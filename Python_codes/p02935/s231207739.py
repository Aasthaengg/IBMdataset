def solve():
  N = int(input())
  V = list(map(int, input().split()))
  ans = 0
  V.sort(reverse=True)
  for i in range(N-1):
    ans += V[i]/pow(2,i+1)
  ans += V[-1]/pow(2,N-1)
  return ans
print(solve())