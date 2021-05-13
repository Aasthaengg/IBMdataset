import math

while 1 :
    a, op, b = raw_input().split()
    a, b = map(int, [a, b])

    if op == "+" :
        print a + b
    elif op == "-" :
        print a - b
    elif op == "*" :
        print a * b
    elif op == "/" :
        print a / b
    else :
        break