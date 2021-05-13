import sys
x = [int(i) for i in input().split()]
x.sort()
print(' '.join(map(str, x)))