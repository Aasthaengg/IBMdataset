n,m = map(int,input().split())
ab = [list(map(int,input().split())) for n in range(m)]
cnt = [0]*n
cnt.insert(0,"X")
for i in range(m):
	for j in range(2):
		cnt[ab[i][j]] += 1
cnt.pop(0)
for s in range(len(cnt)):
	print(cnt[s])