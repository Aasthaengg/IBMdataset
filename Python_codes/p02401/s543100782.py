while True:
    a,op,b = raw_input().split()
    aa = int(a)
    bb = int(b)
    if op == '?':
        break
    elif op == '+':
        print aa + bb
    elif op == '-':
        print aa - bb
    elif op == '*':
        print aa * bb
    elif op == '/':
        print aa / bb