n = int(input())

from collections import defaultdict
d = {0:2,1:1}

def calc(n):
    if n not in d:
        d[n] = calc(n-1) + calc(n-2)
    return d[n]

for i in range(n):
    calc(i)

print(calc(n))