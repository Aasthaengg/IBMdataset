if __name__ == '__main__':
	l = input().split()
	count = 0

	for i in range(len(l)):
		i -= count
		if l[i] == '+':
			l[i - 2] = str(int(l[i - 2])  + int(l[i - 1]))
			l.pop(i - 1)
			l.pop(i - 1)
			count += 2

		elif l[i] == '-':
			l[i - 2] = str(int(l[i - 2])  - int(l[i - 1]))
			l.pop(i - 1)
			l.pop(i - 1)
			count += 2

		elif l[i] == '*':
			l[i - 2] = str(int(l[i - 2])  * int(l[i - 1]))
			l.pop(i - 1)
			l.pop(i - 1)
			count += 2

		else:
			continue
	if len(l) > 1:
		print("Error")
	else:
		print(l[0])

