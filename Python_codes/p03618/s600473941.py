from collections import Counter

a = input()
n = len(a)
c = Counter()
ans = 1
c[a[0]] = 1
for i in range(1, n):
	ans += i - c[a[i]]
	c[a[i]] += 1
print(ans)