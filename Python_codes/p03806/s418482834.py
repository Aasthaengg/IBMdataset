n,ma,mb,*L=map(int,open(0).read().split())
INF=float('inf')
dp=[[INF]*420 for _ in range(420)]
dp[0][0]=0
for a,b,c in zip(*[iter(L)]*3):
	for i in range(400,-1,-1):
		for j in range(400,-1,-1):
			t=dp[i][j]+c
			if dp[i+a][j+b]>t:
				dp[i+a][j+b]=t
ans=INF
_ma,_mb=ma,mb
while _ma<410>_mb:
	ans=min(ans,dp[_ma][_mb])
	_ma+=ma
	_mb+=mb
print(ans if ans<INF else -1)