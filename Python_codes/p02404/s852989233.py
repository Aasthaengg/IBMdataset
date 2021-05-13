put = '#'
put2 = '.'
output = []
while True:
	data = list(map(int, input().split()))
	if data[0] == 0 and data[1] == 0:
		break
	output += [data]

for tmp in output:
	for h in range(tmp[0]):
		for w in range(tmp[1]):
			if h == 0 or h == tmp[0]-1 or w == 0 or w == tmp[1]-1:
				print(put, end="")
			else:
				print(put2, end="")
		print()
	print()
