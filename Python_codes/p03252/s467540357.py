s = input()
t = input()

a = [0 for i in range(26)]
n = len(s)
dict = {}
for i in range(n):
	x = ord(t[i]) - ord("a")
	if s[i] not in dict:
		dict[s[i]] = t[i]
		a[x] += 1
	else:
		if dict[s[i]] != t[i]:
			print ("No")
			exit()

for i in range(26):
	if a[i] >= 2:
		print ("No")
		exit()
print ("Yes")