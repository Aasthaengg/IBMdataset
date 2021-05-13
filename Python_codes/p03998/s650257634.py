a = list(input())
a.append('0')
b = list(input())
b.append('0')
c = list(input())
c.append('0')
p = 0

while True:
    if p == 0:
        y = a.pop(0)
        if len(a) == 0:
            print('A')
            exit(0)
    elif p == 1:
        y = b.pop(0)
        if len(b) == 0:
            print('B')
            exit(0)
    else:
        y = c.pop(0)
        if len(c) == 0:
            print('C')
            exit(0)
    if y == 'a':
        p = 0
    elif y == 'b':
        p = 1
    else:
        p = 2