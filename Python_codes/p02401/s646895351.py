def calc(a, op, b):
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    else:
        r = a / b
    return r
 
while True:
    a, op , b = raw_input().split()
    if op == "?":
        break
    print(calc(int(a), op, int(b)))