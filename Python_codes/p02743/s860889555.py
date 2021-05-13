A, B, C = map(int,input().split())
if C - A - B <= 0:
    print('No')
else:
    if 4*A*B < (C-A-B)**2:
        print('Yes')
    else:
        print('No')

