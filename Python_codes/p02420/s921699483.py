while True:
	char = raw_input()
	if char == "-":
		break
	kaisuu = int(raw_input())
	for i in range(kaisuu):
		num = int(raw_input())
		char1 = char[:num]
		char2 = char[num:]
		char = char2 + char1
	print char