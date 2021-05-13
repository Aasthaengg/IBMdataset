nn = int(input())
ss = input()

ans = 0

for i in range(nn-1):
  n = nn-i
  s = ss[i:]
  a = [0]*n
  a[0] = n
  i, j = 1, 0
  while i < n:
    while i+j < n and s[j] == s[i+j]:
      j += 1
    a[i] = j
    if j == 0:
      i += 1
      continue
    k = 1
    while i+k < n and k+a[k] < j:
      a[i+k] = a[k]
      k += 1
    i += k
    j -= k
  for p in range(1, n-1):
    a[p] = min([p, a[p]])
  sub = max(a[1:])
  if ans < sub:
    ans = sub
print(ans)