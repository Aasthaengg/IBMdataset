#AGC032-B
"""
dp解法。
そこまでにその色で出来た組み合わせの総和がいくつかを保持する配列を
持っておく。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
bef = -1
for i in range(n):
    res = int(readline())
    if bef == res:
        continue
    else:
        lst1.append(res)
        bef = res

n = len(lst1)
lst2 = [-1]*(2*10**5+1)
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    c = lst1[i-1]
    if lst2[c]==-1:
        lst2[c] = i
        dp[i] = dp[i-1]
    else:
        dp[i] = (dp[i-1] + dp[lst2[c]])%(10**9+7)
        lst2[c] = i

print(dp[-1])