import math
def combi(n,r):
  ans = math.factorial(n) // (math.factorial(n-r) * math.factorial(r))
  return ans

N, M = map(int,input().split())

ans = 0
if N > 1:
  ans += combi(N,2)
if M > 1:
  ans += combi(M,2)
print(ans)
