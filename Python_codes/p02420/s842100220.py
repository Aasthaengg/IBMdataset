while True:
	first = input().rstrip()
	if first == '-': break
	
	m = int(input())
	for _ in range(m):
		h = int(input())
		first = first[h:] + first[0:h]

	print(first)
