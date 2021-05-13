s = input()
key = "keyence"
l = len(key)
if s[:l] == key or s[-l:] == key:
	print("YES")
	exit()
for i in range(l):
	if s[:i] == key[:i] and s[-(l-i):] == key[-(l-i):]:
		print("YES")
		exit()
else:
	print("NO")