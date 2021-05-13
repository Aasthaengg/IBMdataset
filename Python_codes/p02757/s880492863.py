n, p = map(int, input().split())
s = list(map(int, list(input())))[::-1]

div = [0 for _ in range(p)]

su = 0
for i in range(n):
	su = (su + s[i] * pow(10, i, p)) % p
	div[su] += 1

cnt = 0
if p in [2, 5]:
	if p == 2:
		ok = [0, 2, 4, 6, 8]
	else:
		ok = [0, 5]

	for i in range(len(s)):
		if s[i] in ok:
			cnt += n - i

else:
	for i in range(len(div)):
		x = div[i]
		if i == 0:
			y = x * (x + 1) // 2
		else:
			y = x * (x - 1) // 2
		cnt += y

print(cnt)