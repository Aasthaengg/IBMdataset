i = 0
while True:
	val = int(raw_input())
	if val == 0:
		break
	else:
		i += 1
		print "Case {0}: {1}".format(i, val)