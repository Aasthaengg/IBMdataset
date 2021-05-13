def check_right_triangle(side1, side2, side3):
	pow = 2
	if side1**pow == side2**pow + side3**pow:
		return True
	if side2**pow == side3**pow + side1**pow:
		return True
	if side3**pow == side1**pow + side2**pow:
		return True
	return False


def check():
	for i in range(int(raw_input())):
		sides = map(int, raw_input().split())
		if check_right_triangle(sides[0], sides[1], sides[2]):
			print "YES"
		else:
			print "NO"



if __name__ == "__main__":
	check()
	# print check_right_triangle(4, 3, 5)
	# print check_right_triangle(4, 3, 6)
	# print check_right_triangle(8, 8, 8)