n = int(input())
s = input()
t = input()

if s == t:
	print(n)
	exit()

maxl = 0
for i in range(n):
	sub_s = s[n-i-1:]
	sub_t = t[:i+1]
	if sub_s == sub_t:
		maxl = max(maxl, i + 1)

print(2 * n - maxl)
