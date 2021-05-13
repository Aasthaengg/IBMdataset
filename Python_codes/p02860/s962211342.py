n = int(input())
s = input()
pre = s[:n//2]
after = s[n//2:]
if n % 2 == 0 and pre == after:
	print('Yes')
else:
	print('No')