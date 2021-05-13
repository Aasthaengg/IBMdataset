s = input()
a = [0 for i in range(26)]
for i in s:
	b = ord(i) - ord("a")
	a[b] += 1
for i in range(26):
	if a[i] == 0:
		x = chr(ord("a")+i)
		s += x
		print (s)
		exit()
a = [0 for i in range(26)]
for i,j in enumerate(reversed(s)):
	b = ord(j) - ord("a")
	a[b] += 1
	if i == 0: continue
	for k in range(b+1,26):
		if a[k] == 1:
			x = chr(ord("a")+k)
			ans = s[:(26-i)-1] + x
			print (ans)
			exit()
print (-1)