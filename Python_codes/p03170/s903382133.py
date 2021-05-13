N,K=map(int,input().split())
a=list(map(int,input().split()))
#dp[i]:=i個の山の時に、直後のプレイヤーの勝ち負け判定（１：勝　０：負）

dp=[-1]*(K+1)
dp[0]=0

for i in range(1,K+1):
    if all(dp[i-a[j]] if i-a[j]>=0 else 1 for j in range(N)):#直後のプレイヤーが取った後の手が全て勝ちパターンなら、負け確定
        dp[i]=0
    else:
        dp[i]=1

print('First' if dp[K] else 'Second')