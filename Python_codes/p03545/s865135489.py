import sys

A = list(map(int,sys.stdin.readline().rstrip()))

from itertools import product

X = ['+','-']
for a in product(X,repeat=3):
    b = A[0]
    for i in range(3):
        if a[i] == '+':
            b += A[i+1]
        else:
            b -= A[i+1]
    if b == 7:
        print(str(A[0])+a[0]+str(A[1])+a[1]+str(A[2])+a[2]+str(A[3])+'=7')
        break
