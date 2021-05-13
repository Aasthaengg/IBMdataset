s = input()
cnt = 0
for b, a in zip(s, reversed(s)):
	if b != a:
		cnt += 1
print(int(cnt / 2))