n = int(input())
inf = float('inf')

M1, M2 = -inf, -inf
m1, m2 = inf, inf

for i in range(n):
  x, y = map(int, input().split())
  d1 = x+y
  d2 = x-y
  M1 = max(M1, d1)
  m1 = min(m1, d1)
  M2 = max(M2, d2)
  m2 = min(m2, d2)

D1 = M1-m1
D2 = M2-m2

print(max(D1, D2))