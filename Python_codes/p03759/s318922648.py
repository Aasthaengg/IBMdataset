import sys

a, b, c = map(int, input().split(' '))

if b - a == c - b:
    print('YES')
    sys.exit()

print('NO')
