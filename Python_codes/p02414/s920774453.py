n,m,l = [int(s) for s in input().split(' ')]
A,B,C = [],[],[]
[A.append([int(s) for s in input().split(' ')]) for i in range(n)]
[B.append([int(s) for s in input().split(' ')]) for i in range(m)]

BT = [[row[i] for row in B] for i in range(l)]
for i in range(n):
	Ci = []
	for j in range(l):
		cij = sum([a*b for a,b in zip(A[i],BT[j])])
		Ci.append(cij)
	C.append(Ci)

C_s = [' '.join([str(i) for i in Ci]) for Ci in C]
[print(row) for row in C_s]