s = input()
lens = len(s)

if s[0] == ">":
	gcnt, lcnt = 0, 1
else:
	gcnt, lcnt = 1, 0
ans = 0

for i in range(lens-1):
	if s[i] == ">":
		if s[i+1] == "<":
			ans += (gcnt*(gcnt-1))//2
			ans += (lcnt*(lcnt-1))//2
			ans += max(gcnt, lcnt)
			gcnt = 1
			lcnt = 0
		else:
			lcnt += 1
	else:
		if s[i+1] == "<":
			gcnt += 1
		else:
			lcnt += 1

ans += (gcnt*(gcnt-1))//2
ans += (lcnt*(lcnt-1))//2
ans += max(gcnt, lcnt)
print(ans)