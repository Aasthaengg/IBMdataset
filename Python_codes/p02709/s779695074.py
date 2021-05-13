import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n,*A = get_all_int()

# dp[i][j] = 活発度高い順のi人目まで処理し、左にjに置いた場合のうれしさの最大
dp = [ [0] * (n+1) for _ in range(n+1) ]

AA = list(enumerate(A))
AA.sort(key=(lambda t: t[1]), reverse=True)

for i, t in enumerate(AA):
    # k 移動前の位置
    # a 活発度
    k,a = t
    for j in range(i+1):
        # 左に置く (すでに左端にj人居る)
        move = abs(k - j)
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + a*move)

        # 右に置く (すでに右端にi-j人居る)
        move = abs(k - (n-(i-j)-1))
        dp[i+1][j] =   max(dp[i+1][j],   dp[i][j] + a*move)

ans = 0

for j in range(n+1):
    ans = max(ans, dp[n][j])

# left = 0
# right = n-1

# AA = list(enumerate(A))
# AA.sort(key=(lambda t: t[1]), reverse=True)
# ans = 0
# for i,a in AA:
#     log(i,a)
#     l = abs(left-i)
#     r = abs(right-i)

#     if l > r:
#         log(f"  {i}->{left}, ", a*l)
#         ans += a * l
#         left += 1
#     else:
#         log(f"  {i}->{right}, ", a*r)
#         ans += a * r
#         right -= 1

print(ans)
