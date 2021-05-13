from itertools import accumulate
from math import pow

X = int(input())

for t, max_d in enumerate(accumulate(range(int(pow(10, 9))))):
    if max_d >= X:
        print(t)
        break
