n,m = map(int, input().split())

if n == 1 or n == 0:
  a = 0
else:
  a = int(n*(n-1)/2)

if m == 1 or m == 0:
  b = 0
else:
  b = int(m*(m-1)/2)

print(a+b)