from collections import defaultdict

def getlist():
	return list(map(int, input().split()))
D = defaultdict(int)
V = []

N, K = getlist()
for i in range(N):
	t, d = getlist()
	V.append([d, t])

V = sorted(V)

ans = []
ex = []
k = 0
for i in range(N):
	x = V[-1 - i][1]
	if k < K:
		if D[x] == 0:
			ans.append(V[-1 - i])
			D[x] += 1
			k += 1
		else:
			ex.append(V[-1 - i])
	else:
		ex.append(V[-1 - i])


if k < K:
	for i in range(K - k):
		ans.append(ex[i])
	eex = []
	for i in range(K - k, len(ex)):
		eex.append(ex[i])
else:
	eex = ex
ans = sorted(ans)
eex = sorted(eex)


A = 0
for i in range(K):
	A += ans[i][0]
A += k * k
n = min(k, N - K)
for i in range(n):
	if ans[i][0] + ((k - i) ** 2) - ((k - i - 1) ** 2) < eex[-1 - i][0]:
		A += eex[-1 - i][0] - ans[i][0] - ((k - i) ** 2) + ((k - i - 1) ** 2)
	else:
		break

print(A)