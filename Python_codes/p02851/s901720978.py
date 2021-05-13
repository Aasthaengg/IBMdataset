from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
	a[i] -= 1

mods = defaultdict(int)
cnt = 0
tmp = 0
for i in range(min(k-1, n)):
	tmp = (tmp+a[i])%k
	mods[tmp] += 1
	cnt += 1

ans = 0
tmp2 = 0
for i in range(n):
	ans += mods[tmp2]
	tmp2 = (tmp2+a[i])%k
	mods[tmp2] -= 1
	if cnt < n:
		tmp = (tmp+a[cnt])%k
		mods[tmp] += 1
		cnt += 1

print(ans)