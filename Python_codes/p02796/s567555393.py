
N = int(input())
L = []

for _ in range(N):
	a, b = map(int, input().split())
	L.append((a-b, a+b))

L = sorted(L, key = lambda x:x[1])
start = L[0][1]
ans = 1

for i in range(1, N):
	if start <= L[i][0]:
		ans += 1
		start = L[i][1]
print(ans)			