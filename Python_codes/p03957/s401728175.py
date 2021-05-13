s = input()
flg = [0,0]

for i in range(len(s)):
	if s[i] == "C":
		if flg[0] == 0:
			flg[0] = 1
		else:
			continue

	if s[i] == "F":
		if flg[0] == 1 and flg[1] == 0:
			flg[1] = 1
		else:
			continue

if flg == [1,1]:
	print("Yes")
else:
	print("No")