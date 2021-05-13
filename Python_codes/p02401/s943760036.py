for i in range(10000):
        a, op, b = input().split()
        if op == '?':
            break
        else:
            if op == '+':
                print(int(a) + int(b))
            elif op == '-':
                print(int(a) - int(b))
            elif op == '*':
                print(int(a) * int(b))
            else:
                print(int(int(a) / int(b)))
