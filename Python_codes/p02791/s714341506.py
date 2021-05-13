n = int(input())
p = list(map(int,input().split()))
cnt = 1
comp = p[0]
for i in range(1,n):
	if comp >= p[i]:
		cnt += 1
		comp = min(comp,p[i])
print(cnt)
