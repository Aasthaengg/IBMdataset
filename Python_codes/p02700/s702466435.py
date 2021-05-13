A, B, C, D = map(int, input().split())
a = A
c = C

while a >= 0:
  c -= B
  if c <= 0:
    print('Yes')
    break
  a -= D
  if a <= 0:
    print('No')
    break