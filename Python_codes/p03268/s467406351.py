n,k=map(int,input().split())
if k % 2 != 0:
  print((n // k) ** 3)
else:
  if n % k >= k // 2:
    print((n // k) ** 3 + (n // k + 1) ** 3)
  else:
    print((n // k) ** 3 + (n // k) ** 3)