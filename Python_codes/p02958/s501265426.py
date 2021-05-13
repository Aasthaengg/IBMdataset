N = int(input())
P = list(map(int, input().split()))
PS = sorted(P)
c = 0
for i in range(N):
	if P[i] != PS[i]:
		c += 1
if c <= 2:
	print('YES')
else:
	print('NO')
