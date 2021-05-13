n = int(input())
a = [0] + list(map(int, input().split()))

G = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
	G[a[i]].append(i)

cnt = 0
for i in range(1, n + 1):
	if a[i] in G[i] and i in G[a[i]]:
		cnt += 1
print(cnt // 2)