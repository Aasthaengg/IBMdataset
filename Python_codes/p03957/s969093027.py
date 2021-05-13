c_f = False
f_f = False
S = input()
for i in range(len(S)):
	if S[i] == "C":
		c_f = True
	if c_f == True and S[i] == "F":
		f_f = True
if c_f == True and f_f == True:
	print("Yes")
else:
	print("No")