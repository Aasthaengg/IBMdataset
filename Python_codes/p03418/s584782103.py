N, K = map(int, input().split())
ans = 0
if K == 0:
  ans = N * N
else:
  for b in range(K+1,N+1):
    k, m = N//b, N%b
    ans += k*(b-K)
    if m != 0:
      ans += max(m-K+1, 0)
print(ans)