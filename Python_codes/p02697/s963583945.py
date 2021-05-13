n, m = map(int, input().split())

if n%2:
  k1, k2 = n//2, n//2+1
  for i in range(m):
    print(k1, k2)
    k1 -= 1
    k2 += 1
else:
  key = [False]*(n)
  key[0] = True
  for i in range(1, n):
    if i == n//2-1 or key[i-1] or key[n-2-i]:
      continue
    key[i] = True
  k1, k2 = n//2, n//2+1
  count = 0
  for i in range(n-1):
    if key[i]:
      print(k1, k2)
      count += 1
    if i%2:
      k1 -= 1
    else:
      k2 += 1
    if count == m:
      break