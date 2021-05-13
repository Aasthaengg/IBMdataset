N = int(input())
K = int(input())
if N > 1:
  x = list(map(int, input().split()))
  ans = 0
  for i in range(N):
    ans += min(2*x[i], 2*(K-x[i]))
else: 
  x = int(input())
  ans = min(2*x, 2*(K-x))
print(ans)