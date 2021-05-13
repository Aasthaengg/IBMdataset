"""
N = list(map(int,input().split()))
S = [str(input()) for _ in range(N)]
S = [list(map(int,list(input()))) for _ in range(h)] 
print(*S,sep="")
"""

import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()
inf = float("inf") # 無限

def reverse(temp):
    out = ""
    for x in temp:
        if x == "U":
            out += "D"
        elif x == "D":
            out += "U"
        elif x == "R":
            out += "L"
        else:
            out += "R"
    return out

sx,sy,tx,ty = map(int,input().split())

A = ""
B = ""
C = ""
D = ""

# A
if sy < ty:
    A += "U" * (ty-sy)
else:
    A += "D" * (sy-ty)
if sx < tx:
    A += "R" * (tx-sx)
else:
    A += "L" * (sx-tx)
B = reverse(A)

C+=B[-1]+A[0]+A+A[-1]+B[0]
D = reverse(C)


print(A+B+C+D)
