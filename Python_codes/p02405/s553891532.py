import sys
while 1:
	H, W = map(int, raw_input().split())
	if H == 0 and W == 0:
		break
	else:
		for h in range(0, H):
			for w in range(0, W):
				if (h + w) % 2 == 0:
					sys.stdout.write("#")
				else:
					sys.stdout.write(".")
			print ""
		print ""