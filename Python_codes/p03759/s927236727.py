import math

A,B,C=list(map(int, input().split()))

if B-A==C-B:
    print('YES')
else:
    print('NO')
