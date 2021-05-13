import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B, C, D = mapint()
from math import gcd

m = C*D//gcd(C, D)
Ccnt = B//C-(A-1)//C
Dcnt = B//D -(A-1)//D
Mcnt = B//m - (A-1)//m

print((B-A)-(Ccnt+Dcnt-Mcnt)+1)