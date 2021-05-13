Ns = []
while True:
	a = input()
	if a == 0:
		break
	else:
		Ns.append(a)

for i, item in enumerate(Ns):
	print "Case {0}: {1}".format(i + 1, Ns[i])