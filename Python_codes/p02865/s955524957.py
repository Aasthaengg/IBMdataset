from collections import defaultdict

n = int(input())

ans = 0
d = defaultdict(int)
for i in range(1, n+1):
	d[i]+=1
	j = n-i
	if d[j] > 0: continue
	if j == i: continue
	if j > 0: ans+=1

print(ans)