j = 0
b = 0

n = int(input())

for i in range(n):
  x, u = input().split()
  if u == 'JPY':
    j += int(x)
  else:
    b += float(x)
print(j + b * 380000)