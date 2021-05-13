import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K = int(input())
from math import gcd
ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        for k in range(1, K+1):
            ans += gcd(i, gcd(j, k))
print(ans)