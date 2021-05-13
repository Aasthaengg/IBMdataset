n, k = map(int, input().split())
c = 0

for i in range(1,n + 1):
	if i % 2 != 0:
		c += 1

if k <= c:
	print("YES")
else:
	print("NO")