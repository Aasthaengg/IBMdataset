from collections import Counter
n = int(input())
s = ["".join(sorted(input())) for _ in range(n)]
k = Counter(s)
ans = 0
for i, j in k.most_common():
	ans += j*(j-1)//2
print(ans)