n = int(raw_input())
dic = {}

for i in xrange(n):
	line = raw_input().split()
	cmd = line[0]
	ope = line[1]
	if cmd == "insert":
		dic[ope] = 1
	else:
		try:
			dic[ope] == 1
		except:
			print("no")
		else:
			print("yes")