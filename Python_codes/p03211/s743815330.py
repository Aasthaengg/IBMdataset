s = input()
answer = 1000

for i in range(0,len(s)-2):
	if answer > abs(753 - int(s[i:i+3])):
		answer = abs(753 - int(s[i:i+3]))

print(answer)