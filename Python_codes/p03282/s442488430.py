s = list(input())
K = int(input())

if set(s[:K]) == {"1"}:
	print("1")
else:
	for ss in s:
		if ss != "1":
			print(ss)
			break
