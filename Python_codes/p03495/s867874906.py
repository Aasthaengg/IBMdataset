from collections import defaultdict

n,k=map(int,input().split())
l=list(map(int,input().split()))
a=defaultdict(int)
for i in l:
	a[i] += 1
a=list(a.items())
if len(a) <= k:
	print(0)
else:
	ans = 0
	a.sort(key = lambda x: x[1])
	for i in range(len(a) - k):
		ans += a[i][1]
	print(ans)
