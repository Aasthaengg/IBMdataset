n, m = map(int, input().split())
ans = 0
if m >= 2*n:
	ans += n
	a = m-2*n
	ans += int(a/4)
else:
	ans += int(m/2)
print (ans)
