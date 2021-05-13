N ,X = list(map(int, input().split()))
L = list(map(int, input().split()))
ans = 1
d = 0
for i in range(N):
	tmp = d + L[i]
	if tmp <= X:
		ans += 1
	d = tmp
print(ans)
