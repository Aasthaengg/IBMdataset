import sys
N, A, B, C, D = map(int, input().split())
s = input()
if C < D:
    for x, y in zip(s[A:], s[A+1:D]):
        if x == '#' and y == '#':
            print('No')
            sys.exit()
    print('Yes')
else:
    for x, y in zip(s[A:], s[A+1:C]):
        if x == '#' and y == '#':
            print('No')
            sys.exit()
    for x, y, z in zip(s[B-2:], s[B-1:], s[B:D+1]):
        if x == '.' and y == '.' and z == '.':
            print('Yes')
            sys.exit()
    print('No')