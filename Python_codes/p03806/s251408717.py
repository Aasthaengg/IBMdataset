# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline #文字列入力のときは注意

n,A,B = [int(i) for i in readline().split()]
abc = [[int(i) for i in readline().split()] for j in range(n)]


res1 = []
res2 = []
eq = 10**9

"""
def dfs(s,g,amari,yen,List):
    global eq
    if s != g:
        a,b,c = abc[s]
        if a*B == A*b:
            eq = min(eq,c)
            dfs(s+1,g,amari,yen,List)
        else: 
            dfs(s+1,g,amari+a*B-b*A,yen+c,List)
            dfs(s+1,g,amari        ,yen,List)
    else:
        if amari != 0:
            List.append((amari,yen))
        else:
            if yen != 0:
                eq = min(eq,yen)
        

dfs(0,n//2,0,0,res1)
dfs(n//2,n,0,0,res2)
"""

def dp(s,g):
    global eq
    d = {0:0}
    for i in range(s,g):
        nd = {}
        a,b,c = abc[i]
#        if a*B == A*b:
#            eq = min(eq,c)
#        else:
        for amari,yen in d.items():
            if amari in nd:
                nd[amari] = min(nd[amari],yen)
            else:
                nd[amari] = yen
            yen += c
            amari += a*B-b*A
            if amari == 0 and yen != 0:
                eq = min(eq,yen)
            elif amari in nd:
                nd[amari] = min(nd[amari],yen)
            else:
                nd[amari] = yen
        d = nd
#        print(d,nd)
    
    return list(d.items())


res1 = dp(0,n//2)
res2 = dp(n//2,n)


#res1.sort()
res2.sort()
#print(res1)
#print(res2)
#print(eq)

from bisect import *

ans = min(10**9,eq)

L = len(res2)
for amari,yen in res1:
    i = bisect(res2,(-amari,-10000000))
    if i < L and res2[i][0] == -amari:
        if 0 < yen+res2[i][1] < ans:
            ans = yen+res2[i][1]


if ans == 10**9:
    print(-1)
else:
    print(ans)




