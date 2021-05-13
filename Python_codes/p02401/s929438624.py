a = []
while True:
    x, op, y = input().split()
    if op == '?':
        break
    x = int(x); y = int(y)
    if op == '+':
        a.append('{}'.format(x+y))
    elif op == '-':
        a.append(x-y)
    elif op == '*':
        a.append(x*y)
    else:
        a.append(x//y)
for x in a:
    print('{}'.format(x))