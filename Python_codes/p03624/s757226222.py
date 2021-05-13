s=list(input())
s=set(s)

for i in range(26):
	if chr(97+i) not in s:
		print(chr(97+i))
		exit()

print('None')