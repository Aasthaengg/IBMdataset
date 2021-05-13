#ABC_049_C_Daydream.py
S = input()
Srev = S[::-1]
# List=["dream","dreamer","erase","eraser"]
Listrev = ["maerd", "remaerd", "esare", "resare"]
can = True
while can == True:
	if Srev == "":
		break
	can = False
	for i in range(4):
		rev=Listrev[i]
		length = len(rev)
		if Srev[0:length] == rev:
			can = True
			Srev=Srev[length:]
if can == True:
	print("YES")
else:
	print("NO")
