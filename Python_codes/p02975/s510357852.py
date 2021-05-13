from collections import Counter
from functools import reduce
from operator import xor
n = int(input())
a = Counter(map(int , input().split()))

if n % 3 == 0:
    if len(a) == 3:
        if 0 == reduce(xor, a) and all(v == n // 3 for v in a.values()):
            print("Yes")
        else:
            print("No")
    elif len(a) == 2:
        if 0 in a and a[0] == n // 3:
            print("Yes")
        else:
            print("No")
    else:
        if 0 in a:
            print("Yes")
        else:
            print("No")
else:
    if len(a) == 1 and 0 in a:
        print("Yes")
    else:
        print("No")