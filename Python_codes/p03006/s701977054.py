import fractions
n = int(input())
z = [list(map(int,input().split())) for _ in range(n)]
if n == 1:
	print(1)
else:
	a = []
	ans = 10**18
	for i in range(n):
		for j in range(i+1, n):
			a.append((z[i][0]-z[j][0], z[i][1]-z[j][1]))
	for i, j in a:
		tmpans = n
		for k, l in z:
			if [k-i, l-j] in z:
				tmpans -= 1
		ans = min(ans, tmpans)
	print(ans)