n = int(input())
a = list(map(int, input().split()))

mean = sum(a) / n
dif = float("inf")
ind = -1
for i in range(n):
	if abs(mean - a[i]) < dif:
		dif = abs(mean - a[i])
		ind = i
print(ind)
