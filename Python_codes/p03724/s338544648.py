N, M = map(int, input().split())
a = [0 for i in range(M)]
b = [0 for i in range(M)]
for i in range(M):
	a[i], b[i] = map(int, input().split())
	a[i] -= 1
	b[i] -= 1

cnt = [0 for i in range(N)]
for i in range(M):
	cnt[a[i]] += 1
	cnt[b[i]] += 1
for i in cnt:
	if i % 2 == 1:
		print("NO")
		break
else:
	print("YES")