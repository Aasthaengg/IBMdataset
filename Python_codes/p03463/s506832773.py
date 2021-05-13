import sys
input = sys.stdin.readline

N, A, B = map(int, input().split(' '))
d = B - A
if d % 2 == 0:
    print('Alice')
else:
    print('Borys')