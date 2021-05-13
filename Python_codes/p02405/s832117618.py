#coding: UTF-8

while True:
	l = raw_input().split()
	H = int(l[0])
	W = int(l[1])

	if H == 0 and W == 0:
		break

	else:
		a = 0
		if H % 2 == 0 and W % 2 == 0:
			while a < H:
				print "#." * int (W / 2) +"\n" +".#" * int (W / 2)
				a += 2
			print 

		if H % 2 == 0 and W % 2 != 0:
			while a < H:
				print "#." * int (W / 2)+"#" +"\n" +".#" * int (W / 2)+"."
				a += 2
			print 

		a = 1
		if H % 2 != 0 and W % 2 == 0:
			while a < H:
				print "#." * int (W / 2) +"\n" +".#" * int (W / 2)
				a += 2
			print"#." * int(W/2) 
			print

		if H % 2 != 0 and W % 2 != 0:
			while a < H:
				print "#." * int (W / 2)+"#" +"\n" +".#" * int (W / 2)+"."
				a += 2
			print"#." * int(W/2)+"#"
			print 