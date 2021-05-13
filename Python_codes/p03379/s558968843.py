n = int(input())
X = list(map(int, input().split()))
XX = sorted(X)
m = n // 2
l = XX[m - 1]
g = XX[m]
for x in X:
	if x <= l:
		print(g)
	else:
		print(l)