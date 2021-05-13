n, m, k = map(int, input().split())
eq_k = False
for p in range(n+1):
  for q in range(m+1):
    area = p * (m - q) + q * (n - p)
    #print(p, q, area)
    if area == k:
      eq_k = True
      break
  if eq_k: break
if eq_k:
  print('Yes')
else:
  print('No')