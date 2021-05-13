import math
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")


A,B,C = LI()
ans = False

gcd = math.gcd(A,B)
if C % gcd ==0:
    ans = True

if ans:
    print('YES')
else:
    print('NO')