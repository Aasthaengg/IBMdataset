while True:
    (a, op, b) = input().split()
    a = int(a)
    b = int(b)
    if op == '?':
        break
    elif op == '+':
        print(a + b)
        pass
    elif op == '-':
        print(a - b)
        pass
    elif op == '*':
        print(a * b)
        pass
    else:
        print(a // b)