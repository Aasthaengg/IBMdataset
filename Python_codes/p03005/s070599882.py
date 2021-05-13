N, K = map(int, input().split())

if K == 1:
  ans = 0
elif N == K:
  ans = 0
else:
  ans = N - K
  
print(ans)