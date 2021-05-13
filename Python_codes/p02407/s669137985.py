num = int(input())
data = list(map(int, input().split()))

output = []
lengh = len(data)
for tmp in range(lengh):
	output += [data.pop(-1)]

for tmp in output:
	if tmp == output[-1]:
		print(tmp)
	else:
		print(tmp, end=" ")
