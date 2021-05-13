s = input()
for i in s:
	if i =="C":
		for j in s[s.index("C"):]:
			if j =="F":
				print("Yes")
				exit()

print("No")