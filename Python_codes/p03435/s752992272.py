from itertools import product
c = [list(map(int, input().split())) for i in range(3)]

"""
a0 = 0 とする
すると
b0 = c00 - a0
b1 = c01 - a0
b2 = c02 - a0
"""

a = [0, None, None]
b = [c[0][i] - a[0] for i in range(3)]

a[1] = c[1][0] - b[0]
a[2] = c[2][0] - b[0]

f = True
for i in range(3):
    for j in range(3):
        if c[i][j] != a[i]+b[j]:
            f = False
            break
if f:
    print('Yes')
else:
    print('No')
    
