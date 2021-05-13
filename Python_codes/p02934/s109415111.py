n = int(input())
a = [int(i) for i in input().split()]
ans = 0

for i in range(n):
	a[i] = 1/a[i]
	ans += a[i]
print(1/ans)