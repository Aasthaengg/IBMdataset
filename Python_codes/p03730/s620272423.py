a, b, c = map(int, input().split())
d = a % b
A = {d}
while d != 0:
  d += a
  d %= b
  A.add(d)
print('YES' if c in A else 'NO')