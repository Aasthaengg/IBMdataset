from collections import defaultdict,deque
import numpy as np
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,K = inpl()
AA = np.array(inpl())
S = sum(AA)

koho = set()
for i in range(1,int(math.sqrt(S))+3):
    if S%i == 0:
        koho.add(i)
        koho.add(S//i)

koho = sorted(list(koho))
ans = 0
for k in koho:
    AA_modk = sorted(AA%k)
    #print(k,AA_modk)

    Ln = Rn = 0
    L = 0
    R = N-1
    while L <= R:
        if Ln <= Rn:
            Ln += AA_modk[L]
            L += 1
        else:
            Rn += k - AA_modk[R]
            R -= 1

    #print(Ln,Rn)

    if K >= Ln:
        ans = max(k,ans)

print(ans)
