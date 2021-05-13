import sys
 
c = 0
for line in sys.stdin:
	if line[0] == '0':
		break
	c+=1
	print 'Case %s: %s' %(c,line),