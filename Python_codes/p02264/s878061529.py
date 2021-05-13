data = raw_input().split()
n = int(data[0])
q = int(data[1])

queue = []
for i in range(n):
	process = raw_input().split()
	process[1] = int(process[1])
	queue.append(process)

time = 0
while len(queue) > 0:
	if queue[0][1] > q:
		queue[0][1] -= q
		time += q
		queue.append(queue[0])
	else:
		time += queue[0][1]
		print("{:} {:}".format(queue[0][0], time))
	del queue[0]