n, k = map(int, input().split())
s = input()

change = [0]
for i, (e1, e2) in enumerate(zip(s, s[1:])):
	e1 = int(e1)
	e2 = int(e2)
	if e1 ^ e2:
		change.append(i + 1)

change.append(n)
end = len(change) - 1

ans = 0
for i, l in enumerate(change[:-1]):
	if s[l] == "1":
		ri = min(i + 2 * k + 1, end)
	else:
		ri = min(i + 2 * k, end)

	r = change[ri]

	ans = max(ans, r - l)

print(ans)
