N, M = map(int, input().split())
cnt = [0] * N
for i in range(M):
	a, b = map(lambda x: int(x) - 1, input().split())
	cnt[a] += 1
	cnt[b] += 1

for i in range(N):
	if cnt[i] % 2 != 0:
		print("NO")
		exit()
print("YES")