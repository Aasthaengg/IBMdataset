import sys

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    print('NO')
    sys.exit()

d = abs(A-B)
v = V - W
if d/v <= T:
    print('YES')
else:
    print('NO')

