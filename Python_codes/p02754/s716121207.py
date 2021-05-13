n, a, b = [int(i) for i in input().split()]
cnt = n // (a + b) * a
if n % (a + b) >= a:
  cnt += a
else:
  cnt += n % (a + b)
print(cnt)