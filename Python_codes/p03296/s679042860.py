n = int(input())
a = list(map(int, input().split()))

ans = 0
tmp = ""
cnt = 0
for i in range(n):
	if a[i] == tmp:
		cnt += 1
	else:
		ans += (cnt+1) // 2
		tmp = a[i]
		cnt = 0

ans += (cnt+1) // 2

print(ans)