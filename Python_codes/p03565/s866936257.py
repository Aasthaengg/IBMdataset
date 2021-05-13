Sp = input()
T = input()

if len(T) > len(Sp):
	print("UNRESTORABLE")
	exit()
	
oklist = []
for i in range(len(Sp) - len(T), -1, -1):
	for j in range(len(T)):
		if Sp[i + j] != "?" and Sp[i + j] != T[j]:
			break
	else:
		okpre = ["a" if Sp[k] == "?" else Sp[k] for k in range(i)]
		oksuf = ["a" if Sp[k] == "?" else Sp[k] for k in range(i + len(T), len(Sp))] 
		oklist.append("".join(okpre) + T + "".join(oksuf))

if oklist:
	print(min(oklist))
else:
	print("UNRESTORABLE")