while True:
  a, op, b = input().split()
  a, b = int(a), int(b)
  if op == '+':
    print(a + b)
    next
  elif op == '-':
    print(a - b)
    continue
  elif op == '*':
    print(a * b)
    continue
  elif op == '/':
    print(a // b)
    continue
  else:
    break
