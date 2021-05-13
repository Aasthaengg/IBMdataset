import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
S = list(input())
T = list(input())
from math import gcd

leng = N*M//gcd(N, M)
step = (leng//N)*(leng//M)//gcd((leng//N), (leng//M))

for i in range(1, leng+1, step):
    if (i-1)%(leng//N)==0 and(i-1)%(leng//M)==0:
        if S[(i-1)//(leng//N)]!=T[(i-1)//(leng//M)]:
            print(-1)
            break
else:
    print(leng)