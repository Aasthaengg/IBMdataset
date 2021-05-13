while True:
    a,op,b = raw_input().split()
    if '?' == op:
        exit()
    a = int(a)
    b = int(b)
    if '+' == op:
        print a + b
    if '-' == op:
        print a - b
    if '*' == op:
        print a * b
    if '/' == op:
        print a / b