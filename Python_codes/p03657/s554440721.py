A, B = map(int, input().split())
if (A+B) % 3 and A % 3 and B % 3:
    print('Impossible')
else:
    print('Possible')

