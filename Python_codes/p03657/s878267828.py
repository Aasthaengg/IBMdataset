a_can, b_can = map(int, input().split())

if (a_can + b_can) % 3 == 0:
    print('Possible')
elif a_can % 3 == 0:
    print('Possible')
elif b_can % 3 == 0:
    print('Possible')
else:
    print('Impossible')