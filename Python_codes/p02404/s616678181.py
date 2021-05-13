import sys
while 1:
	H, W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	else:
		for h in range(0, H):
			for w in range(0, W):
				if h == 0 or h == H - 1 or w == 0 or w == W -1:
					sys.stdout.write("#")
				else:
					sys.stdout.write(".")
			print ""
		print ""