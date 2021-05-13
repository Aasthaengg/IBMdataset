def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
h = [0]+ LI()
#h[i]はi番目の高さ
#0-indexedにしておくと考えにくいので1-indexedにしておく
#dp[i]は足場iにいくのに必要な最小コスト
dp = [0]*(n+1)
#これも1-indexedにしておく
dp[1] = 0
dp[2] = abs(h[2]-h[1])
#2番目の足場に移るのは1番目の足場からいくしかないのでわけて考える
#最初蛙は足場1にいるため最小コストは0としておく
for i in range(3,n+1):
    dp[i] = min(dp[i-2]+abs(h[i]-h[i-2]), dp[i-1]+abs(h[i]-h[i-1]))
print(dp[n])