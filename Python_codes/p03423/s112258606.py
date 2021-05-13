import math
#import numpy


def readints():
    return list(map(int, input().split()))


n = int(input())
if n == 0:
    print(0)
    exit()

print(n//3)
