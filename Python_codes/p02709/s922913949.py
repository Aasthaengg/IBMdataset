from collections import defaultdict

#dpa[(0,0)] = 0

n = int(input())

a = list(map(int, input().split()))

d = {}
for i in range(n):
	d[i] = a[i]

dp = defaultdict(lambda: 0)

i = 0
x = 0
y = 0
maxr = 0
for k,v in sorted(d.items(), key=lambda x: -x[1]):
	i+=1
#	print(k,": ",v)
	for j in range(i+1):
		if j == 0:
			migi = 0
		else:
			migi = abs(n - j - k)*v
		
		if i - j == 0:
			hida = 0
		else:
			hida = abs(k - (i - j)+1)*v
		dp[(j,i-j)] = max(dp[(j-1,i-j)]+migi,dp[(j,i-j-1)]+hida)
		
		if i == n:
			maxr = max(maxr,dp[(j,i-j)])
#		print(j,i-j,k,hida,migi,dp[(j,i-j)])

print(maxr)