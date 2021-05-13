import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//math.factorial(n-r)*math.factorial(r)


m = int(input())
print(24+(24-m))
