while True:
  aopb = [x for x in input().split()]
  a = int(aopb[0])
  op = aopb[1]
  b = int(aopb[2])
  if op == '?':
    break
  elif op == '+':
    print(a + b)
  elif op == '-':
    print(a - b)
  elif op == '*':
    print(a * b)
  elif op == '/':
    print(a // b)