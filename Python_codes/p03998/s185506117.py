a = list(input())
b = list(input())
c = list(input())

s = a[0]

del a[0]

while True:
    if s is 'a':
        if len(a) == 0:
            print('A')
            break

        s = a[0]
        del a[0]
        
    elif s is 'b':
        if len(b) == 0:
            print('B')
            break
        
        s = b[0]
        del b[0]
        
    else:
        if len(c) == 0:
            print('C')
            break
        
        s = c[0]
        del c[0]