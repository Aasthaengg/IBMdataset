i = 100
for i in range (i):
    a_list = [str(x) for x in input().split()]
    a = int(a_list[0])
    b = int(a_list[2])
    op = a_list[1]
    if op == '+':
        ab = a + b
        print(ab)
        i = i + 1
        continue
    elif op == '-':
        ab = a - b
        print(ab)
        i = i + 1
        continue
    elif op == '*':
        ab = a * b
        print(ab)
        i = i + 1
        continue
    elif op == '/':
        ab = a // b
        print(ab)
        i = i + 1
        continue
    elif op == '?':
        exit()

