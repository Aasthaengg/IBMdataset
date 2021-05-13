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

n,c = m()

time = [[0 for i in range(31)] for j in range(10**5+2)]

popopo = [[] for i in range(30)]

for i in range(n):
    s,t,c = m()
    popopo[c-1].append([s,t])


for i in range(30):
    popopo[i].sort()
    
for i in range(30):
    for j in range(len(popopo[i])):
        s,t = popopo[i][j]
        if time[s][i+1] == 0:
            time[t][i+1] = 1
            time[s-1][0] += 1
            time[t][0] -= 1
        else:
            time[t][i+1] = 1
            time[s][0] += 1
            time[t][0] -= 1

ma = time[0][0]
for i in range(1,10**5+2):
    time[i][0] += time[i-1][0]
    ma = max(ma,time[i][0])
print(ma)


