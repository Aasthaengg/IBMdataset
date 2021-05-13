N, L = map(int, input().split())

m = 10 ** 9
pre = 0
for i in range(N):
  t = L + i
  pre += t
  
  if abs(t) < abs(m):
    m = t

print(pre - m)
