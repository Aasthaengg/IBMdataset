N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
A_sum = sum(A)
B_sum = 0
n, m = N, 0
ans= 0
while m != M:
  if A_sum + B_sum <= K:
    ans = max(ans, n+m)
    m += 1
    B_sum += B[m]
  elif A_sum + B_sum > K and n >= 0:
    A_sum -= A[n]
    n -= 1
  else:
    break
if A_sum + B_sum <= K:
  ans = max(ans, n+m)    
print(ans)