s = input()
l = len(s)
for i in range(l):
	for j in range(i, l):
		if s[:i] + s[j:] == "keyence":
			print("YES")
			exit()
else:
	print("NO")