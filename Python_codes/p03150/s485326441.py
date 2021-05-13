s = list(input())
n = len(s)

if "".join(s) == "keyence":
	print("YES")
	exit()

for i in range(n):
	ss = s[::]
	for j in range(i, n):
		ss.pop(i)
		if "".join(ss) == "keyence":
			print("YES")
			break
	else:
		continue
	break
else:
	print("NO")