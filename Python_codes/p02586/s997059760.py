import sys,collections as cl,bisect as bs,heapq as hq
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

r,c,k = m()


item = [[0 for j in range(c)] for i in range(r)]



for i in range(k):
    R,C,V = m()
    item[R-1][C-1] = V


dp = [[0 for k in range(4)] for j in range(c)]
dpo = [[0 for k in range(4)] for j in range(c)]
for i in range(r):
    for j in range(c):
        if j == 0:
            if item[i][j] != 0:
                po = 0
                for kk in range(4):
                    po = max(po,dpo[j][kk])
                for k in range(4):
                    if k == 0:
                        dp[j][k] = po
                    elif k == 1:
                        dp[j][k] = po + item[i][j]
                    else:
                        dp[j][k] = 0

            else:
                po = 0
                for kk in range(4):
                    po = max(po,dpo[j][kk])
                for k in range(4):
                    if k == 0:
                        dp[j][k] = po
                    else:
                        dp[j][k] = 0

        else:
            if item[i][j] != 0:
                po = 0
                for kk in range(4):
                    po = max(po,dpo[j][kk])
                for k in range(4):
                    if k == 0:
                        dp[j][k] = max(dp[j-1][k],po)
                    elif k == 1:
                        dp[j][k] = max(dp[j-1][k],dp[j-1][0] + item[i][j],po + item[i][j])
                    else:
                        dp[j][k] = max(dp[j-1][k],dp[j-1][k-1] + item[i][j])

            else:
                po = 0
                for kk in range(4):
                    po = max(po,dpo[j][kk])
                for k in range(4):
                    if k == 0:
                        dp[j][k] = max(dp[j-1][k],po)
                    else:
                        dp[j][k] = dp[j-1][k]
    for j in range(c):
        for k in range(4):
            dpo[j][k] = dp[j][k]
            dp[j][k] = 0


ans = 0

for i in range(4):
    ans = max(ans,dpo[-1][i])
print(ans)
