N, M = map(int, input().split())
AB = [0 for _ in range(N)]
for i in range(M):
	a, b = map(int, input().split())
	AB[a-1] += 1
	AB[b-1] += 1
for i in range(N):
	if AB[i]%2 or AB[i]%2:
		print("NO")
		exit()
print("YES")