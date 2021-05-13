import sys
A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
x = 0

if A > B:
    x = A
    A = B
    B = x

# Bが逃げ切るとき
if V <= W:
    print('NO')
    sys.exit()

if T*V+A-B >= T*W:
    print('YES')
else:
    print('NO')
