n = int(input())
a = list(map(int,input().split()))
a.sort()
maxkouho = a[-1]
k = maxkouho/2
maxans = 10**18
ans = 0
for i in range(n-1):
	s = abs(a[i]-k)
	if s < maxans:
		maxans = s
		ans = a[i]
print(maxkouho, ans)