N, K = map(int, input().split())
p = 0
for i in range(1, N+1):
  if i>=K:
    p += 1/N
  else:
    c = 0
    while i<K:
      i *= 2
      c += 1
    p += (1/N)*(0.5)**c
print(p)