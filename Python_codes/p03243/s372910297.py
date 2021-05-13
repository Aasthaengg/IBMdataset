import sys

def I(): return int(sys.stdin.readline().rstrip())

N = I()
A = [111*i for i in range(1,10)]

for i in range(9):
    if N <= A[i]:
        print(A[i])
        break