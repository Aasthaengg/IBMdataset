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
    if len(x) == 0:
        return []
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

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

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

a,b,c,d,e,f = m()

wa = [0 for i in range(f+1)]
su = [0 for i in range(f+1)]

wa[0] = 1
su[0] = 1


for i in range(f//100 + 1):
    if i*100 + a*100 <= f:
        wa[i*100 + a*100] = max(wa[i*100 + a*100],wa[i*100])
    if i*100 + b*100 <= f:
        wa[i*100 + b*100] = max(wa[i*100 + b*100],wa[i*100])

for i in range(f + 1):
    if i+c <= f:
        su[i + c] = max(su[i + c],su[i])

    if i+d <= f:
        su[i + d] = max(su[i + d],su[i])


#po = [[0,a,0],[0,b,0]]
po = []

for i in range(1,f+1):
    for j in range(f+1):
        if i+j <= f and wa[i] and su[j] and (i //100) * e >= j:
            po.append([(100*j)/(i+j),i+j,j])

po.sort(reverse = True)


print(po[0][1],po[0][2])