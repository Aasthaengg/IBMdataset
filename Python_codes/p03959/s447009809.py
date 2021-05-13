MOD = 10 ** 9 + 7
n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 1

if t[0] > a[0] or t[-1] < a[-1] or t[-1] != a[0]:
	ans *= 0

for i in range(1, n - 1):
	if t[i - 1] != t[i]:
		if t[i] > a[i]:
			ans *= 0
			break
		else:
			continue
	if a[i + 1] != a[i]:
		if t[i] < a[i]:
			ans *= 0
			break
		else:
			continue
	ans = (ans * min(t[i], a[i])) % MOD

print(ans)