import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


A,B,C,D = MI()

from math import gcd


def f(n):
    return n-n//C-n//D+n//((C*D)//gcd(C,D))


print(f(B)-f(A-1))
