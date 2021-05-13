n = int(input())
x = list(map(int, input().split()))

ans = float("inf")

for p in range(min(x),max(x)+1):
	t = 0
	for i in x:
		t+=(i-p)**2
	ans = min(ans, t)

print(ans)