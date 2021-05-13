while True:
    a,op,b = input().split()
    A = int(a)
    B = int(b)
    if op == "+":
        print(A + B)
    elif op == "-":
        print(A - B)
    elif op == "*":
        print(A * B)
    elif op == "/":
        print(A // B)
    else:
        break