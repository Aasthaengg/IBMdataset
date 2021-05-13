while True:
    line = raw_input().split()
    a = int(line[0])
    op = str(line[1])
    b = int(line[2])
    if op == '+':
        print a + b
    elif op == '-':
        print a - b
    elif op == '*':
        print a * b
    elif op == '/':
        print int(a / b)
    elif op == '?':
        break