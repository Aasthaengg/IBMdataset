import sys
from io import StringIO
import unittest
import math

def resolve():
    inp = input()
    li = list(map(lambda x: int(x), inp.split(" ")))
    a = li[0]
    b = li[1]
    k = li[2]
    g = math.gcd(a, b)

    for i in range(g,0,-1):
        if g%i == 0:
            k -= 1
        if k == 0:
            print(i)
            break
            
resolve()