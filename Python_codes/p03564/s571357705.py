N, K = [int(input()) for i in range(2)]

v = 1
for i in range(N):
  a = v*2
  b = v+K
  v = min(a, b)

print(v)