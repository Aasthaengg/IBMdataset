s = input()
i = 0
count = 0
one_flag = False
while i < len(s):
	if one_flag == False:
		one_flag = True
		i += 1
		count += 1
	else:
		if s[i] == s[i - 1]:
			if i == len(s) - 1:
				break
			else:
				one_flag = False
				i += 2
				count += 1
		else:
			i += 1
			count += 1
print(count)