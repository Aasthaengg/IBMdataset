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

n = onem()

a = l()

p = -Max
po = 0

pp = Max
ppo = 0


for i in range(n):
    if a[i] >= p:
        p = a[i]
        po = i+1
    if a[i] <= pp:
        pp = a[i]
        ppo = i+1

if abs(p) >= abs(pp):

    print(2*n-1)
    for i in range(1,n+1):
        print(po,i)
    for i in range(1,n):
        print(i,i+1)

else:

    print(2*n-1)
    for i in range(1,n+1):
        print(ppo,i)
    for i in range(n,1,-1):
        print(i,i-1)










