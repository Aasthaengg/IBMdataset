a, b, c, dis = map(int, input().split())

judge = abs(a - b) <= dis and abs(b - c) <= dis


if (abs(a - c) <= dis or judge):
    print('Yes')
else:
    print('No')