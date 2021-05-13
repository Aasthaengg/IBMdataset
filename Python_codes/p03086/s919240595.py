s = list(input())
count = 0
answer = 0

for i in range(len(s)):
	if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
		count += 1
	else:
		count = 0
	if count > answer:
			answer = count

print(answer)