l = input()
col = l.split(' ')
a = int(col[0])
op = col[1]
b = int(col[2])

if 1 <= a <= 10 ** 9 and 1 <= b <= 10 ** 9:
  if op == '+':
    print(a + b)
  elif op == '-':
    print(a - b)
