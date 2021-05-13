while True:
    a, op, b = list(input().split())
    if op == '?':
        break

    a = int(a)
    b = int(b)
    ans = 0

    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '*':
        ans = a * b
    elif op == '/':
        ans = a // b

    print(ans)
