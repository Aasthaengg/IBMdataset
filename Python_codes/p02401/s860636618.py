AOPB = input().split()
a = int(AOPB[0])
b = int(AOPB[2])
op = AOPB[1]
while op != "?":
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
    AOPB = input().split()
    a = int(AOPB[0])
    b = int(AOPB[2])
    op = AOPB[1]