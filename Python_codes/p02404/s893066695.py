import sys
line = sys.stdin.readline()
while line:
	H,W = map(int,line.split())
	if H == 0 and W == 0:
		break;
	print "#"*W
	for i in range(0,H-2):
		print "#"+"."*(W-2)+"#"
	print "#"*W
	print ""
	line = sys.stdin.readline()