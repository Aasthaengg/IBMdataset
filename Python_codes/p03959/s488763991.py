n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
renew = [0] * n
b = 0
for i, h in enumerate(t):
	if b < h:
		if h > a[i]:
			print(0)
			exit()
		renew[i] = 1
		b = h
b = 0
for i, h in enumerate(a[::-1]):
	if b < h:
		if h > t[n - i - 1]:
			print(0)
			exit()
		renew[n - i - 1] = 1
		b = h
ans = 1
for f, th, ah in zip(renew, t, a):
	if not f:
		ans *= min(th, ah)
		ans %= mod
print(ans)