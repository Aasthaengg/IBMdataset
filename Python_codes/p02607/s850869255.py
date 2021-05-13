N = int(input())
a = list(map(int,input().split()))

ans = 0
k = 1
for i in a:
	if k % 2 == 1:
		if i % 2 == 1:
			ans += 1
	k += 1
print(ans)