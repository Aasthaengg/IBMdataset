import sys

for line in sys.stdin:
    [a, op, b] = line.split()
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    else:
        break