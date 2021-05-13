S = ""
while 1:
	try:
		s = raw_input()
	except:
		break
	S += s.lower()

for i in range(ord('a'), ord('z')+1):
	print '%s : %d' %(chr(i), S.count(chr(i)))