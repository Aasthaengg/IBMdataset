while True:
	num_str = input()
	if num_str == "0":
		break;

	sum = 0
	for num in list(num_str):
		sum += int(num)
	print(sum)