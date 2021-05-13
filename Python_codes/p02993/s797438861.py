s=list(str(input()))
f=True
for i in range(1,4):
	if s[i-1]==s[i]:
		f=False
		break
	else:
		continue
if f:
	print("Good")
else:
	print("Bad")