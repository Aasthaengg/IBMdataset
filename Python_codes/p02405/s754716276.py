import sys
line = sys.stdin.readline()
while line :
	H,W = map(int,line.split())
	if H == 0 and W == 0:
		break;
	for i in range(0,H):
		for j in range(0,W):
			if (i+j)%2 == 0:
				sys.stdout.write("#")
			else:
				sys.stdout.write(".")
		print ""	
	print ""
	line = sys.stdin.readline()