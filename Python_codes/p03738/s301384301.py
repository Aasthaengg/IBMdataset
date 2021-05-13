a = input()
b = input()
c = len(a)
d = len(b)
if c>d:
    print('GREATER')
elif c<d:
    print('LESS')
else:
    for x, y in zip(a,b):
        if x<y:
            print('LESS')
            exit()
        if x>y:
            print('GREATER')
            exit()
    print('EQUAL')