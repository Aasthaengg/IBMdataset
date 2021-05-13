#coding: UTF-8

while True:
	l = raw_input().split()

	H = int(l[0])
	W = int(l[1])

	if H == 0 and W == 0:
		break

	else :
		a = 1
		print "#" * W
		x = "#"+"." * (W-2)+"#"

		while a < H - 1:
			print x
			a += 1

		print "#" * W + "\n"