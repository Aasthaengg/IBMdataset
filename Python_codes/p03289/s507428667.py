S = input()
flag = 1
if S[0] != "A":
	flag = 0
elif S[2:-1].count("C") != 1:
	flag = 0
else:
	idx = S[2:-1].find("C")
	S2 = S[1:idx+2]+ S[idx + 3:]
	if not S2.islower():
		flag = 0

if flag == 1:
	print("AC")
else:
	print("WA")

