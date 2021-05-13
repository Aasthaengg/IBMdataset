import sys
from io import StringIO
import unittest
import math

def resolve():
    s,c= map(int,input().split())

    if s>=c/2:
        print(str(math.floor(c/2)))
    else:
        zanc = c - (s * 2)
        print(str(s + math.floor(zanc/4)))
        
resolve()