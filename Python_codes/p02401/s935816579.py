while(True):
    vals = input().split()
    a = int(vals[0])
    op = vals[1]
    b = int(vals[2])

    if op == '?': break
    if op == '+': print(a + b)
    if op == '-': print(a - b)
    if op == '*': print(a * b)
    if op == '/': print(a // b)