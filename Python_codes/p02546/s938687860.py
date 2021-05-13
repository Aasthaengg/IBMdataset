s = list(input())

if s[-1] != 's':
    [print(m, end='') for m in s]
    print('s')
else:
    [print(m, end='') for m in s]
    print('es')