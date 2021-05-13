a, b, c = map(int, input().split())
import math
if a + b >= c:
    print('No')
else:
    if a * b * 4 < (c - a - b) ** 2:
        print('Yes')
    else:
        print('No')