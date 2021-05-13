ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
n,m,q = ma()
L_rs=[[] for i in range(n)]
for i in range(m):
    l,r=ma()
    L_rs[l-1].append(r-1)
for i in range(n):
    L_rs[i].sort()
# print(L_rs)
def isok(num,val):##適宜変更
    return num<=val
def bisect(ls,val): ##valの関数isok(x,val)がTrueとなる一番右のindex を返す 全部Falseなら-1,Trueならlen(ls)-1
    ok = -1
    ng = len(ls)
    x = (ok+ng)//2
    while ng-ok>1:
        num = ls[x]
        if isok(num,val):
            ok = x
        else:
            ng = x
        x = (ok+ng)//2
    return ok ##一番右のTrueのindex  Trueの個数はok+1こ

ans = [[0]*(n+1) for i in range(n+1)]
for r in range(n):
    for l in range(r,-1,-1):
        ans[l][r]=ans[l+1][r] + bisect(L_rs[l],r)+1

for i in range(q):
    l,r=ma()
    print(ans[l-1][r-1])
