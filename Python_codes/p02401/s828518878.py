while True:
    n = input().split()
    a,b = int(n[0]),int(n[2])
    if n[1] == '+':
        print(a + b)
    elif n[1] == '-':
        print(a - b)
    elif n[1] == '*':
        print(a * b)
    elif n[1] == '/':
        print(a // b)
    else:
        if n[1] == '?':
            break