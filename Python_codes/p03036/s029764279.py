import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//math.factorial(n-r)*math.factorial(r)


r, D, x = map(int, input().split())
xx = []
xx.append(r*x-D)
print(r*x-D)
for i in range(9):
    a = r*xx[i]-D
    print(a)
    xx.append(a)
