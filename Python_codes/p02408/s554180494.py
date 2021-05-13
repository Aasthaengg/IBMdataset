x = input()
S = [1,2,3,4,5,6,7,8,9,10,11,12,13]
H = [1,2,3,4,5,6,7,8,9,10,11,12,13]
C = [1,2,3,4,5,6,7,8,9,10,11,12,13]
D = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in range(x):
	mark, num = map(str, raw_input().split())
	if mark == 'S':
		S.remove(int(num))
	elif mark == 'H':
		H.remove(int(num))
	elif mark == 'C':
		C.remove(int(num))
	elif mark == 'D':
		D.remove(int(num))
for i in range(len(S)):
	print "S " + str(S[i])
for i in range(len(H)):
	print "H " + str(H[i])
for i in range(len(C)):
	print "C " + str(C[i])
for i in range(len(D)):
	print "D " + str(D[i])