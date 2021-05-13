import sys
A,B,X = map(int,input().split())
if not ( 1 <= A <= 100 and 1 <= B <= 100 and 1 <= X <= 200 ):
    sys.exit()

if (B + A) >= X and A <= X:
    print('YES')
else:
    print('NO')