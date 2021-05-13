X = str(input())

Tn = 0
Sn = 0
Nagasa = len(X)

for i in range (0, Nagasa):
	if X[i] == 'T':
		if Sn == 0:
			Tn+=1
		else:
			Sn-=1
	else:
		Sn+=1

print(2*Tn)		