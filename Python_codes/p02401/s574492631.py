import math

while True:
    a, op, b = map(str, input().split())
    a = int(a)
    b = int(b)
    if 0 <= a and b < 20001:
        if op == "+":
            answer = a + b
            print(answer)
        elif op == "-":
            answer = a - b
            print(answer)
        elif op == "*":
            answer = a * b
            print(answer)
        elif op == "/":
            answer = a / b
            print(math.floor(answer))
        elif op == "?":
            break
    else:
        if op == "?":
            break
        else:
            continue