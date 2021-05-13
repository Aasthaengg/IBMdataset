n = int(input())
S = [0] * 13
H = [0] * 13
C = [0] * 13
D = [0] * 13
for i in range(n):
	mark,val = raw_input().split()
	val = int(val)
	if mark=="S":
		S[val-1] = 1
	elif mark=="H":
		H[val-1] = 1
	elif mark=="C":
		C[val-1] = 1
	else: # mark=="D"
		D[val-1] = 1

for i in range(0,13):
	if S[i]==0: print "S %s" % (i+1)
for i in range(0,13):
	if H[i]==0: print "H %s" % (i+1)
for i in range(0,13):
	if C[i]==0: print "C %s" % (i+1)
for i in range(0,13):
	if D[i]==0: print "D %s" % (i+1)