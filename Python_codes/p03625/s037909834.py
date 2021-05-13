import sys
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
C = sorted(C.items(), reverse=True)
a, b = 0, 0
for k, v in C:
    if a == 0 and v >= 4:
        print(k * k)
        sys.exit()
    if v >= 2:
        if a == 0:
            a = k
        elif b == 0:
            print(a * k)
            sys.exit()
print(0)