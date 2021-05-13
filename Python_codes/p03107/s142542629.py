s = input()
c = max(s.count("1") - s.count("0"),s.count("0") - s.count("1"))

if len(s) == 1:
	print(0)
else:
	print(len(s)-c)


