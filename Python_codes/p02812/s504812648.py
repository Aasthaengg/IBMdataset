input()
string = input()

count = 0

for i in range(len(string)):
	if string[i] == 'A':
		if i < len(string)-2 and string[i+1] == 'B':
			if string[i+2] == 'C':
				count += 1


print(count)