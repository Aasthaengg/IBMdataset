W = raw_input().lower()
T = []
while 1:
	try:
		T += raw_input().lower().split()
	except:
		break
print T.count(W)