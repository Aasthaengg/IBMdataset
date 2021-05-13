s = input()
streak = 0
nowst = 0
ls = {"A", "C", "G", "T"}
for i in s:
	if i in ls:
		nowst += 1
		streak = max(nowst, streak)
	else:
		nowst = 0
print(streak)