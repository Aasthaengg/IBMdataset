import sys

def I():
    return int(sys.stdin.readline().rstrip())

N = I()

A = [1,2,3,5,6,9,10,13,17]
if N in A:
    print('No')
else:
    print('Yes')