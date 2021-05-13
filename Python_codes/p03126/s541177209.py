n,m=map(int,input().split())
cnt=[n for _ in range(m)]
for i in range(n):
	k = list(map(int,input().split()))
	for i in range(1, k[0]+1):
		cnt[k[i]-1] -= 1
ans = 0
for i in range(m):
	if cnt[i] == 0:
		ans += 1
print(ans)