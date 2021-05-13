s = 0
n = int(input())
for i in range(n):
  x, u = input().split()
  x = float(x)
  if u == 'JPY':
    s += x
  else:
    s += 380000 * x
print(s)
