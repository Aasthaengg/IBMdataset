a = input()
b = input()
c = input()
ch = 'a'
while True:
    if ch == 'a':
        if len(a) == 0:
            print('A')
            exit()
        ch = a[0]
        a = a[1:]
    elif ch == 'b':
        if len(b) == 0:
            print('B')
            exit()
        ch = b[0]
        b = b[1:]
    elif ch == 'c':
        if len(c) == 0:
            print('C')
            exit()
        ch = c[0]
        c = c[1:]