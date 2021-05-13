n = input()
array = []
base = 0
for i in range(n):
	inst = raw_input().split()
	if inst[0][0] == 'i':
		array.append(int(inst[1]))
	elif inst[0] == "delete":
		if int(inst[1]) in array:
			x = array[::-1].index(int(inst[1]))
			if x != -1 and int(inst[1]):
				del array[-x-1]
	elif inst[0][6] == 'F':
		array.pop()
	else:
		base += 1
print (" ".join(map(str,array[base:][::-1])))