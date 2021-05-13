a, b = map(int, input().split())

if a*b-int(a*b/2)*2 == 0:
    print('Even')
else:
    print('Odd')