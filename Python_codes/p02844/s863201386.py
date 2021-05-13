ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
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

n = ni()
s = input()
idxs =[[] for i in range(10)]
for i in range(n):
    num= int(s[i])
    idxs[num].append(i)
ans = 0
for i in range(10):
    if not idxs[i]:
        continue
    i0 = idxs[i][0]
    for j in range(10):
        t1 = bisect(idxs[j],i0)
        if t1==len(idxs[j])-1:
            continue
        i1 = idxs[j][t1+1]
        for k in range(10):
            t2 = bisect(idxs[k],i1)
            if t2==len(idxs[k])-1:
                continue
            else:
                ans+=1
                #print(i,j,k)
print(ans)
