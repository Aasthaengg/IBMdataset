from collections import Counter, defaultdict
import numpy as np

N, P = map(int, input().split())
A = list(map(int, input().split()))
A = [i % 2 for i in A]

d = defaultdict(int)
d.update(Counter(A).items())

if d[1] == 0:
    if P == 0:
        print(2**N)
    else:
        print(0)
else:
    print(2**(N-1))