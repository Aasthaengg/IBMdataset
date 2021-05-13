n = int(input())
l = list(map(int, input().split()))
s = sum(l)
a, b = 0, 0

while l:
  m1 = max(l)
  a += m1
  l.remove(m1)
  if l:
    m2 = max(l)
    l.remove(m2)
print( 2 * a - s )

