from collections import defaultdict

d = defaultdict(int)
D = defaultdict(lambda:1)
N = int(input())

ans = 1
C = int(input())
d[C] += 1
c = C

for i in range(N - 1):
	C = int(input())
	d[C] += 1
	if C == c:
		pass
	else:
		if d[C] >= 2:
			ans = (ans + D[C]) % 1000000007
	D[C] = ans
	c = C

print(ans)