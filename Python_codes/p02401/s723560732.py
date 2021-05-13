def calc(a, op, b):
    if op == '+':
        return(a + b)
    if op == '-':
        return(a - b)
    if op == '*':
        return(a * b)
    if op == '/':
        return(a / b)
while True:
    a, op, b = raw_input().split()
    if op == '?':
        break
    print(calc(int(a), op, int(b)))