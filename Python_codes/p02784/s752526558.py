H, n = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
for x in arr:
	sum += x
print("Yes" if sum >= H else "No")