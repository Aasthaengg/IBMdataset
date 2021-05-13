a, b = list(input().split())

if a == 'H':
    print(b)
elif a == 'D':
    if b == 'H':
        print('D')
    else:
        print('H')