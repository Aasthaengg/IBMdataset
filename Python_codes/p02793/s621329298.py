import sys
stdin = sys.stdin
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
from fractions import gcd

mod = 10**9+7

n = ni()
a = na()
b,c = 1,0

def lcm(m,n):
    return (m*n)//gcd(m,n)

for i in a:
    b=lcm(b,i)

for i in a:
    c+=b//i

print(c%mod)