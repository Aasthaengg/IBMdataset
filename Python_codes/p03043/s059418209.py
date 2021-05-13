from math import log2
def solve():
  N, K = map(int, input().split())
  ans = 0
  for i in range(1,N+1):
    if i>=K:
      ans += 1/N
    else:
      a = -(-log2(K/i)//1)
      ans += 1/((pow(2,a))*N)
  return ans
print(solve())