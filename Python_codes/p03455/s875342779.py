a, b = map(int, input().split())
if 1 <= a <= 10000 and 1 <= b <= 10000:
    if (a * b)%2 == 0:
        print('Even')
    else:
        print('Odd')