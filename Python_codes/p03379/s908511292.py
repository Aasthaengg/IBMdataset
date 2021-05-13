n = int(input())
x = [int(i) for i in input().split()]
y = sorted(x)
a = y[n // 2 - 1]
b = y[n // 2]
for i in x:
  if i <= a:
    print(b)
  elif i >= b:
    print(a)