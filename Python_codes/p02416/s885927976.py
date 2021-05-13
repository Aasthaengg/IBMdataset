import sys
import math

while 1:
    n = input()

    if (n == 0):
        break

    ret = 0

    while n > 0:
        ret += n % 10
        n /= 10

    print ret