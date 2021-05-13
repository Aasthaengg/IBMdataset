while True:
    (a, op, b) = [int(i) if i.isdigit() else i for i in input().split()]

    if op == '?':
        break

    if op == '+':
        print(a + b)

    if op == '-':
        print(a - b)

    if op == '*':
        i = a * b
        print(a * b)

    if op == '/':
        print(a // b)