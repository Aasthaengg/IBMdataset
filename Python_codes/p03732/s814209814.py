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

n,w = m()

po = [[] for i in range(4)]
pr = [[0] for i in range(4)]

for i in range(n):
    a,b = m()
    if i == 0:
        coo = a
        po[0].append(b)
    else:
        kkk = a - coo
        po[kkk].append(b)

for i in range(4):
    po[i].sort(reverse = True)
    for ii in range(len(po[i])):
        pr[i].append(pr[i][-1] + po[i][ii])

co = 0
su = 0
for i in range(len(po[0]) + 1):
    for ii in range(len(po[1]) + 1):
        for iii in range(len(po[2]) + 1):
            for iiii in range(len(po[3]) + 1):
                if (i * coo + ii * (coo + 1) + iii * (coo + 2) + iiii * (coo + 3)) <= w:
                    su = max(su,pr[0][i]+pr[1][ii]+pr[2][iii]+pr[3][iiii])

print(su)




