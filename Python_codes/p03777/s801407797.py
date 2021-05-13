import sys
a, b = map(str, input().split())
if (a, b) == ('H', 'H'):
    print('H')
    sys.exit()
if (a, b) == ('D', 'D'):
    print('H')
    sys.exit()
else:
    print('D')