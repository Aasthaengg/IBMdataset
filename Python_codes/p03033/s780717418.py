import sys
import bisect
from heapq import heappop, heappush, heapify
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N,Q= map(int,input().split())
STX = [list(map(int,input().split())) for i in range(N)]
D = [int(input()) for i in range(Q)]

'''
import random
N = 2*10**5
Q = 2*10**5
STX = []
for i in range(N):
    S,T = sorted([random.randint(0,10**9-1) for i in range(2)])
    if S == T:
        T += 1
    X = random.randint(1,10**9)
    STX.append([S,T,X])
D = sorted([random.randint(0,10*9) for i in range(Q)])
'''

inf = 10**15
PFXS = [(s-x,True,x) for s,t,x in STX]
PFXT = [(t-x,False,x) for s,t,x in STX]
PFX = PFXS + PFXT
PFX.append((-inf,True,inf))
PFX.append((inf,False,inf))
PFX.sort()

addq = [inf]
delq = [inf+1]
iterD = iter(D)

d = next(iterD)
for p,f,x in PFX:
    while d < p:
        ans = addq[0] if not addq[0] == inf else -1
        print(ans)
        try:
            d = next(iterD)
        except:
            exit()
    if f:
        heappush(addq, x)
    else:
        heappush(delq, x)
    while addq[0] == delq[0]:
        heappop(addq)
        heappop(delq)




