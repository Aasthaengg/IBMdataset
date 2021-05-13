import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
from decimal import Decimal
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

D = I()
C = LI()
s = [LI() for _ in range(D)]

T = [I() for _ in range(D)]
#print(D,C)
#print(s)
#print(T)
def last(d,i):
    T_d = T[:d]
    n = [j for j, x in enumerate(T_d,1) if x == i]
    if n:
        #print(T_d,i,"n=",n)
        return max(n)
    else:
        return 0
        
        
score = 0
for d in range(1,D+1):
    sum_c = 0
    for i in range(1,26+1):
        sum_c += C[i-1] * (d -last(d,i))
    score += s[d-1][T[d-1]-1] - sum_c
    print(score)
