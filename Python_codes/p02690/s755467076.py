X = int(input())
Rg = 1000
#print(1000**5)
#print(2**5)
for a in range(Rg):
	A = a**5
	for b in range(Rg): 
		B = b**5
		if A-B==X:
			print(a,b)
			exit()
		if A+B==X:
			print(a,-b)
			exit()