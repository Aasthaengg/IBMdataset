# A - Prefix and Suffix
n = int(input())
s = input()
t = input()

if len(s) + len(t) <= n:
	print(n)
elif s == t and len(s) >= n:
	print(len(s))
else:
	min_len = min(len(s), len(t))
	ans = len(s) + len(t)
	
	for i in range(1, min_len + 1):
		if s[-i:] == t[:i]:
			ans = len(s) + len(t) - i
	
	if ans < n:
		ans = n
	
	print(ans)