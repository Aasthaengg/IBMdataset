from queue import Queue

class Process:
	def __init__(self, name, time):
		self.name = name
		self.time = int(time)

	def set_time(self, time):
		self.time = time

n, q = map(int, input().split())
queue = Queue()
for i in range(n):
	name, time = map(str, input().split())
	queue.put(Process(name, time))

time_elapsed = 0
while queue.empty() != True:
	process = queue.get()
	time = process.time
	if time > q:
		process.set_time(time - q)
		time_elapsed += q
		queue.put(process)
	else:
		time_elapsed += min(time, q)
		print(process.name + ' ' + str(time_elapsed))
