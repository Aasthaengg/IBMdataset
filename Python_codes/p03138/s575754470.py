n, k = map(int, input().split())
a = list(map(int, input().split()))

d = [0] * 40
for i in range(n):
  for j in range(40):
    if a[i] & (1<<j):
      d[j] += 1
s = 0
for i in range(39,-1,-1):
  if s + 2**i > k:
    continue
  if d[i] > n//2:
    continue
  s += 2**i

res= 0
for i in range(n):
  res += a[i] ^ s
print (res)
