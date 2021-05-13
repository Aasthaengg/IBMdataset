n = int(input())
A = []
f = 0
s = 0
for _ in range(n):
  a = int(input())
  A.append(a)
  if f <= a:
    s = f
    f = a
  elif s <= a:
    s = a
for a in A:
  if a == f:
    print(s)
  else:
    print(f)
