n = int(input())
#n = int(lines.pop())

dictionary = dict()
for i in range(n):
	command,data = input().split()
	#command,data = lines.pop().split()
	if command == 'insert':
		dictionary[data] = 1
	else:
		if data in dictionary:
			print('yes')
		else:
			print('no')