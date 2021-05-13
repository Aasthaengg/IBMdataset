import collections
import itertools
import numpy as np
import sys
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N,A,B = IL()

if (B-A)%2 == 0:
    print("Alice")
else:
    print("Borys")