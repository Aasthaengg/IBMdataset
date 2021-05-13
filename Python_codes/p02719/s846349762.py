n,k = map(int, input().split())

if n >= k:
  ans_a = n % k
  ans_b = abs(n %k - k)
  ans = min(ans_a, ans_b)
else:
  if n >= abs(n-k):
    ans = abs(n-k)
  else:
    ans = n

print(ans)