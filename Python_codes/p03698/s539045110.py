s = input()
length = len(s)

for i in range(length):
	for j in range(i+1,length):
		if s[i] == s[j]:
			print("no")
			exit()

print("yes")