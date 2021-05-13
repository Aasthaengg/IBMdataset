#ABC113-D Number of Amidakuji
"""
問題：
W本長さHの棒に任意に横線を引く時に、
1からスタートしてkにたどり着くあみだくじの通り数を求めよ
ただし、横線には以下の制約がある
同じ高さに何本引いても良いが、その端点が隣接してはいけない
同じ高さ同士にしか引けない
隣り合う棒にしか引けない
解法：
dpを用いて解く。
dp[i][j]:高さiの状態にいる時の、棒jにたどり着く通り数
dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1]の三通りの遷移について、
(これは横線は必ず端点を共有しないことから言える)
それぞれあり得る通り数を全探索して足していった結果が答え。
最終的にd[h][k]が答え
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7
h,w,g = map(int,readline().split())

dp = [[0]*w for _ in range(h+1)]
dp[0][0] = 1

def func(x):
    if x <= 0:
        return 1
    return func(x-2) + func(x-1)

for i in range(h):
    for j in range(w):
        for k in range(-1,2): #左下、直下、右下
            if not 0 <= j + k < w:
                continue
            #func:右側,左側の自由な状態の棒間の数を入れてやる
            if k == -1:
                l = max(0,j-2)
                r = max(0,w-1-(j+1))
            elif k == 0:
                l = max(0,j-1)
                r = max(0,w-1-(j+1))
            else:
                l = max(0,j-1)
                r = max(0,w-1-(j+2))
            dp[i+1][j+k] += dp[i][j]*func(l)*func(r)
            dp[i+1][j+k] %= mod


print(dp[h][g-1])