
import sys
def I(): return int(sys.stdin.readline().rstrip())

A = [I() for i in range(6)]
if A[4]-A[0] > A[-1]:
    print(':(')
else:
    print('Yay!')