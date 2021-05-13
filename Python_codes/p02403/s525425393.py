put = '#'
output = []
while True:
	data = list(map(int, input().split()))
	if data[0] == 0 and data[1] == 0:
		break
	output += [data]

for tmp in output:
	for h in range(tmp[0]):
		for w in range(tmp[1]):
			print(put, end="")
		print()
	print()
