while True:
    Input = input().split()
    a = int(Input[0])
    op = Input[1]
    b = int(Input[2])
    if a >= 0 and b >= 0 and a <= 20000 and b <= 20000:
        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            if b != 0:
                print(int(a / b))
        elif op == "?":
            break