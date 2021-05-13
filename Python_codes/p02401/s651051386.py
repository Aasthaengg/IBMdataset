while True:
    l = input().split()
    a = int(l[0])
    b = int(l[2])
    op = l[1]
    if op == '?':
        break
    if op == '+':
        ans = a + b
        print(ans)
    elif op == '-':
        ans = a - b
        print(ans)
    elif op == '*':
        ans = a * b
        print(ans)
    elif op == '/':
        ans = a // b
        print(ans)