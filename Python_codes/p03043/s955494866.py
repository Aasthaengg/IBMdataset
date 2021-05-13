import sys
from fractions import Fraction

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = LI()


kakuritu = []
for i in range(1,N+1):
    count = 0
    while i < K:
        i *= 2
        count += 1
    kakuritu.append(N*(2**count))
result = 0
for kaku in kakuritu:
    result += Fraction(1, kaku)


print(result.numerator / result.denominator)