s = input()

for i in range(97,123):
	if not chr(i) in s:
		print(chr(i))
		exit()

print("None")