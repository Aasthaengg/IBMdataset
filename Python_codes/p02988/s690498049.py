n = int(input())
p = list(map(int,input().split()))
ans = 0
for j in range(n-2):
	if p[j] < p[j+1] < p[j+2] or p[j+2] < p[j+1] < p[j]:
		ans += 1
print(ans)