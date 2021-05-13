import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

h,w = m()
n = onem()

a = l()

po = [[0 for i in range(w)] for j in range(h)]


co = 0

for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[co] == 0:
                co += 1
            po[i][j] = co + 1
            a[co] -= 1
    else:
        for j in range(w-1,-1,-1):
            if a[co] == 0:
                co += 1
            po[i][j] = co + 1
            a[co] -= 1

for i in range(h):
    print(jo(po[i]))







