while 1:
    a , op, b = raw_input().split()
    a = int(a)
    op = str(op)
    b = int(b)

    if op == '+':
         print a+b
    elif op == '-':
         print a-b
    elif op == '*':
        print a*b
    elif op == '/':
        print a/b
    elif op == '?':
        break