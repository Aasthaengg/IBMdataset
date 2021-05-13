import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
from math import gcd
g = 0
ans = 1
for _ in range(N):
    t = int(input())
    g = gcd(t, ans)
    ans = t*ans//g
print(ans)