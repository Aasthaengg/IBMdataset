import sys

queue = []

header = sys.stdin.readline()
(n, q) = header.strip().split()
q = int(q)

for line in sys.stdin.readlines():
  (name, time) = line.strip().split()
  queue.append((name, int(time)))

total_time = 0
while len(queue) > 0:
  (name, time) = queue.pop(0)
  time -= q
  if time > 0:
    total_time += q
    queue.append((name, time))
  else:
    total_time += time + q
    print "%s %s" % (name, total_time)