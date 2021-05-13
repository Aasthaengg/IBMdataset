n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
m = min(n, m)
while m > 0:
	arr.pop()
	m -= 1
ans = 0
for x in arr:
	ans += x
print(ans)