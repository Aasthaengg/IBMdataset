n,k=map(int,input().split())
a=list(map(int,input().split()))
dp=[False]*(k+1)
# dp[i]:残り石i個で自分のターンになった時、勝てるならTrue
# dp[0]=False,dp[a]=True,求めるのはdp[k]
# dp[i]={dp[i-a]の中にひとつでもFalseがあればTrue、other->False}
# <=> すべてのai(in a)についてdp[i]=False->dp[i+ai]=True
for i in range(k+1):
      for ai in a:
            if i+ai<=k and not dp[i]:
                  dp[i+ai]=True
print('First' if dp[k] else 'Second')