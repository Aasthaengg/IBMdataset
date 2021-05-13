a = input()
b = input()
c = input()

la = len(a)
lb = len(b)
lc = len(c)

na = 1
nb = 0
nc = 0

now = a[0]

while True:
    if now == 'a':
        if na == la:
            print('A')
            break
        else:
            now = a[na]
            na += 1
    elif now == 'b':
        if nb == lb:
            print('B')
            break
        else:
            now = b[nb]
            nb += 1
    else:
        if nc == lc:
            print('C')
            break
        else:
            now = c[nc]
            nc += 1