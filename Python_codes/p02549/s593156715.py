n,k= list(map(int, input().strip().split()))
l=[0]*n
r=[0]*n
mod=998244353
for i in range(k):
    l[i],r[i] = list(map(int, input().strip().split()))

dp = [0]*(n+1)
dp[1] = 1
dpsum = [0]*(n+1)
dpsum[1] = 1
for i in range(2,n+1):
    for j in range(k): # 各kにおいてli~riまでの移動量が＋となる場合の和を計算する
        li = i - r[j] # 遷移元のindexの左端を求める
        ri = i - l[j] # 遷移元のindexの右端を求める
        if ri < 0: # riがﾏｲﾅｽの場合はそもそも以降を考えない
            continue
        li = max(li,1) # li がﾏｲﾅｽの場合があるので、そのときのindexはｽﾀｰﾄの"1"と考える
        dp[i] += dpsum[ri] - dpsum[li-1] # li~riの和を足す
    dpsum[i] = (dpsum[i-1]+dp[i])%mod
    
print(dp[n]%mod)