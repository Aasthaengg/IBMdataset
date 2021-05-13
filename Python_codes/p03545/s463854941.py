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


a = list(_S())
a = list(map(int,a))
l = len(a)-1

for i in range(1<<l):
    t = a[0]
    sign = ['-','-','-']
    # 符号のループ
    for j in range(l):
        # i を j回右にシフトして1との論理積を取り、0であれば+とする
        if (i >> j) & 1 == 0:
            t += a[j+1]
            sign[j]='+'
        else:
            t -= a[j+1]
    # print(t)
    if t == 7:
        break

ans = str(a[0])
for i in range(l):
    ans += sign[i] + str(a[i+1])
ans += '=7'
print(ans)