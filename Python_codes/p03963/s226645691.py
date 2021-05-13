# ABC_046_B_AtCoDeerくんとボール色塗り.py

N,K = list(map(int, input().split()))
ans=K
if N!=1:
	for i in range(2,N+1):
		ans*=(K-1)
print(ans)