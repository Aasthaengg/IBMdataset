n = int(input())
d, x = map(int, input().split())
a = 0
for i in range(n):
  c = int(input())
  t = c
  a += 1
  j = 1
  while c + 1 <= d:
    a+= 1
    j += 1
    c = t * j
a += x
print(a)