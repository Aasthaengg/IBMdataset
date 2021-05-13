import math

A, B = map(int, input().split())

if A % 2 == B % 2:
    K = abs(B - A) / 2
    if A > B:
        print(A - math.ceil(K))
    else:
        print(B - math.ceil(K))
else:
    print('IMPOSSIBLE')
