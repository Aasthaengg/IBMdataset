N = int(input())
a = 2
b = 1
for i in range(N-1):
  c = a + b
  a = b
  b = c
if N ==1:
  print(b)
else:
  print(c)