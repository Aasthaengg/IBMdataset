queue = []

n, q = map(int, input().split())
for i in range(n):
  name, time = input().split()
  queue.append([name, int(time)])

t = 0
while len(queue) > 0:
  entry = queue.pop(0)
  t += min(entry[1], q)
  entry[1] -= q
  if entry[1] > 0:
    queue.append(entry)
  else:
    print("{} {}".format(entry[0], t))