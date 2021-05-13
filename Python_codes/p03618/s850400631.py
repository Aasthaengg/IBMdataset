from collections import Counter
a = input()
n = len(a)
c = Counter(a).most_common()
ans = 1
tmp = 0
for i, j in c:
	ans += tmp * j
	tmp += j
print(ans)