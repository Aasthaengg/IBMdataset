n, k = map(int, input().split())
p = list(map(int, input().split()))

arr = [(1 + m) / 2 for m in p]
ans = 0
sum = 0
for i in range(n):
	sum += arr[i]
	if i >= k: sum -= arr[i - k] 
	ans = max(ans, sum)
print(ans)
