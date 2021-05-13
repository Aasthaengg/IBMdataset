from sys import stdin
import sys

n = int(stdin.readline().rstrip())

A = [0, 0, 0]
for i in range(n):
    B = [int(j) for j in stdin.readline().rstrip().split()]

    t = B[0]-A[0]
    x = abs(B[1]-A[1])
    y = abs(B[2]-A[2])

    z = x+y

    if t % 2 == 1:
        if not(z % 2 == 1 and z <= t):
            print("No")
            sys.exit()

    else:
        if not(z % 2 == 0 and z <= t):
            print("No")
            sys.exit()

    A = B

print ("Yes")






