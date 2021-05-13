def calc(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a // b

while True:
    str_list = input().split()
    a = int(str_list[0])
    op = str_list[1] 
    b = int(str_list[2])

    if op == "?":
        break

    print(calc(a, op, b))