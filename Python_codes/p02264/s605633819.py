a = raw_input()
n, q = a.split(" ")
n = int(n)
q = int(q)
total = 0

queue = []
for i in range(n):
	queue.append(raw_input())
while (len(queue) > 0):
	b = queue.pop(0)
	p, t = b.split(" ")
	sa = int(t) - q
	if sa > 0:
		queue.append(p + " " + str(sa))
		total += q
	else:
		total += int(t)
		print (p + " " + str(total))