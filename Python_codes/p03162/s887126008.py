from sys import stdin,stdout

n = int(stdin.readline())
ls = list()
dp1 = [0] * n
dp2 = [0] * n
dp3 = [0] * n
for i in range(n):
	a, b, c = map(int, stdin.readline().split())
	if i == 0:
		dp1[0] = a
		dp2[0] = b
		dp3[0] = c
	else:
		dp1[i] = max(dp2[i - 1], dp3[i - 1]) + a
		dp2[i] = max(dp1[i - 1], dp3[i - 1]) + b
		dp3[i] = max(dp1[i - 1], dp2[i - 1]) + c
print(max(dp1[n - 1], dp2[n - 1], dp3[n - 1]))
