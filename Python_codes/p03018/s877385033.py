s = input()
s = s.replace("BC","Z")
cnt = 0
c = 0
for i in s:
	if i == "A":
		c += 1
	elif i == "Z":
		cnt += c
	else:
		c = 0
print (cnt)