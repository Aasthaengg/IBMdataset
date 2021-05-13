from collections import Counter
n = int(input())
a = sorted([int(x) for x in input().split()])
freq = Counter(a)
A = max(a)
good = [True]*(A+1)
ans = 0
for x in freq:
	for k in range(2*x,A+1,x):
		good[k] = False
	if good[x] and freq[x]==1:
		ans += 1
print(ans)