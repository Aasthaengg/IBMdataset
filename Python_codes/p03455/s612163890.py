a, b = map(int, input().split())
if (1 <= a & a <= 10000) & (1 <= b & b <= 10000):
    multi = a * b
    if multi % 2 != 0:
        print('Odd')
    elif multi % 2 == 0:
        print('Even')