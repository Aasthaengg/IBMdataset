s = input()
for i in range(97,97 + 26):
	if chr(i) not in  s:
		print(chr(i))
		exit()
print('None')