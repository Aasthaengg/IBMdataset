s =input()
c = False
f = False
for i in s:
	if i == "C":
		c = True
	elif i == "F" and c:
		f = True
print("Yes" if c and f else "No")