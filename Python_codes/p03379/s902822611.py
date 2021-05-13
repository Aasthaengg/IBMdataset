n = int(input())
x = list(map(int,input().split()))
a = x[:]
a.sort()
kijun = a[n//2]
a1 = a[n//2]
a2 = a[n//2-1]
for i in x:
	if i < kijun:
		print(a1)
	else:
		print(a2)