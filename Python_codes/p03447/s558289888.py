import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//math.factorial(n-r)*math.factorial(r)


x = int(input())
a = int(input())
b = int(input())

print((x-a) % b)
