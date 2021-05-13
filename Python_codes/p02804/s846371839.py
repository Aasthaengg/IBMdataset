MOD, ans = 10**9+7, 0
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
kai, gai = [1], [1]
for i in range(n):
	kai.append((kai[i] * (i+1)) % MOD)
	gai.append(pow((kai[i] * (i+1)) % MOD, MOD-2, MOD))
for i in range(n):
	x, y = 0, 0
	if i <= (n-k):
		x = (a[i] * kai[n-i-1] * gai[n-i-k] * gai[k-1]) % MOD
	if i >= (k-1):
		y = (a[i] * kai[i] * gai[i-k+1] * gai[k-1]) % MOD
	ans = (ans + y - x) % MOD
print(ans)