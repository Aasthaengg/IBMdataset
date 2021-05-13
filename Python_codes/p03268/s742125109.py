N, K = map(int, input().split())

if K % 2 == 0:
  n = (N+(K//2)) // K
  ans = n**3 + (N//K)**3
else:
  n = N // K
  ans = n ** 3
print(ans)