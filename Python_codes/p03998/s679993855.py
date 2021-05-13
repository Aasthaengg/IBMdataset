a = input()
b = input()
c = input()

t = 'a'
while True:
    if t == 'a':
        if a == '':
            print('A')
            exit()
        t = a[0]
        a = a[1:]
    elif t == 'b':
        if b == '':
            print('B')
            exit()
        t = b[0]
        b = b[1:]
    else:
        if c == '':
            print('C')
            exit()
        t = c[0]
        c = c[1:]
