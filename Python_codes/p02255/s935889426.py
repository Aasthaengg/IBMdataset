#input number
n = raw_input()

if n < 1 and n > 100:
	exit()

# input elements
l = raw_input()

elements = [int(e) for e in l.split()]

print ' '.join(str(e) for e in elements)

for i in range(1, int(n)):
	key = elements[i]
	j = i - 1
	while j >= 0 and elements[j] > key:
		elements[j + 1] = elements[j]
		j -= 1
	elements[j + 1] = key
	# output
	print ' '.join(str(e) for e in elements)