while True:
    l = list(input().split())
    a = int(l[0])
    op = l[1]
    b = int(l[2])
    
    if op == "?":
        break
    
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)