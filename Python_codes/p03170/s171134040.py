import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
#n,k=100,100000
#a=range(1,101)

dp=[False for _ in range(k+1)]
calted=[False for _ in range(k+1)]
# dp[i]:残り石i個で自分のターンになった時、勝てるならTrue
# dp[0]=False,dp[a]=True,求めるのはdp[k]
mi=min(a)
ma=max(a)
for ai in a:
	dp[ai]=True
	calted[ai]=True
# dp[i]={dp[i-a]の中にFalseがあればTrue、すべてTrueならFalse}
for i in range(mi+1,k+1):
      if calted[i]:
            continue
      il=[i-ai for ai in a if i-ai>=0]
      f=1
      for l in il:
        f*=dp[l]
      if f == 0:
            dp[i]=True
      else:
            dp[i]=False
print('First' if dp[k] else 'Second')
#print(dp)
#print(datetime.datetime.now())