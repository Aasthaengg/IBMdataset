def print_list(lst) :
	lst = ' '.join(list(map(str, lst)))
	print(lst)

while True:
	H,W = list(map(int, input().split()))
	if (H == 0) and (W == 0):
		break
	else:
		for n in range(0, H):
			s = ""
			for m in range(0, W):
				if (n % 2 == 1 and  m % 2 == 1 ) or (n % 2 == 0 and m % 2 == 0):
					s += "#"
				else :
					s += "."
			print(s)
		print("")