S = raw_input()

if len(S) == 2:
	print S
elif len(S) == 3:
	print "".join([i for i in reversed(S)])
