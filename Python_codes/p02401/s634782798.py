for i in range(10000):
  x = input().split()
  a = int(x[0])
  op = x[1]
  b = int(x[2])
  if op == "+":
    A = a + b
    print(A)
  elif op == "-":
    B = a - b
    print(B)
  elif op == "*":
    C = a * b
    print(C)
  elif op == "/":
    D = a // b
    print(D)
  elif op == "?":
    break
