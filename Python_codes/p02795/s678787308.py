from math import ceil

h = int(input())
w = int(input())
n = int(input())

if h >= w:
    print(ceil(n/h))
else:
    print(ceil(n/w))