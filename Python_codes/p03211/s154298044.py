s = input()
min_difference = 999
for i in range(len(s)-2):
	abs3 = abs(753 - int(s[i:i+3]))
	if abs3 < min_difference:
		min_difference = abs3
print(min_difference)
