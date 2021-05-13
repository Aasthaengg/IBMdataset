import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from math import gcd
def resolve():
    x = int(input())
    g = gcd(x, 360)
    print(360 // g)
resolve()