from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations,groupby
import sys
import bisect
import string
import math
import time
import random
def S_():
    return input()
def LS():
    return [i for i in input().split()]
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def bit_combination(k,n=2):
    rt=[]
    for tb in range(n**k):
        s=[tb//(n**bt)%n for bt in range(k)]
        rt+=[s]
    return rt
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
#sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

def ran_input():
    import random
    n=random.randint(4,16)
    rmin,rmax=1,10
    a=[random.randint(rmin,rmax) for _ in range(n)]
    return n,a

show_flg=False
show_flg=True

ans=1

n,k=LI()
a=[]

for i in range(n):
    x,y=LI()
    a.append((x,y))

a.sort()

ans=inf

for lx in range(n):
    for rx in range(lx+1,n):
        for ly in range(n):
            for ry in range(ly+1,n):
                c=0
                x1,x2,y1,y2=a[lx][0],a[rx][0],a[ly][1],a[ry][1]
                if y1>y2:
                    y1,y2=y2,y1
                for i in range(lx,rx+1):
                    x,y=a[i]
                    if x1<=x<=x2 and y1<=y<=y2:
                        c+=1
                
#                show(c,(lx,rx),(ly,ry),(x1,x2,y1,y2))
                if c>=k:
                    ans=min(ans,(x2-x1)*(y2-y1))

print(ans)

