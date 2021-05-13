n = raw_input()
while 1:
	try :
		a = map(int,raw_input().split())
		a.sort()
		a.reverse()
#		print a
		if a[0]**2 == a[1]**2 + a[2]**2:
			print "YES"
		else : 
			print "NO"
	except EOFError:
		break