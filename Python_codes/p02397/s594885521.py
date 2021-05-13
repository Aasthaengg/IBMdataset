x = []
y = []
i = 0

while True:
  a, b = map(int, input().split())
  if b < a:
    stock = a
    a = b
    b = stock
  x.append(a)
  y.append(b)
  if x[i] == 0 and y[i] == 0:
    break
  i += 1

for j in range(i):
  print(str(x[j]), str(y[j]))