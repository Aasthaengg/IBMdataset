a, op, b = input().split()

a, b = map(int, (a, b))

if op == "+":
    print(a+b)
else:
    print(a-b)
