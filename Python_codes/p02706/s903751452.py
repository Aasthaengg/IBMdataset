n,m = map(int,input().split())
arr = [int(x) for x in input().split()]
sm = 0
for i in arr:
	sm+=i 
if sm<=n:
	print(n-sm)
else:
	print(-1)