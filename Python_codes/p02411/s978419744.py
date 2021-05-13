while True:
	numlist = list(int(i) for i in input().split())
	mid = numlist[0]
	final = numlist[1]
	retest = numlist[2]

	sum = mid + final

	if mid == -1 and final == -1 and retest == -1:
		break

	if mid == -1 or final == -1:
		print("F")	
	elif sum >= 80:
		print("A")
	elif 80 > sum >= 65:
		print("B")
	elif 65 > sum >= 50:
		print("C")
	elif 50 > sum >= 30 and retest < 50:
		print("D")
	elif 50 > sum >= 30 and retest >= 50:
		print("C")
	elif sum < 30:
		print("F")