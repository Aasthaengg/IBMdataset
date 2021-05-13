from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a).most_common()
ans = 0
for i, j in c:
	if j < i:
		ans += j
	elif j > i:
		ans += j-i
print(ans)