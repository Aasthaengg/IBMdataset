from queue import Queue
n,q = map(int,input().split())
names = []
times = []
for _ in range(n):
  data = list(map(str,input().split()))
  names.append(data[0])
  times.append(int(data[1]))

names_queue = Queue()
times_queue = Queue()
for i in range(n):
  names_queue.put(names[i])
  times_queue.put(times[i])
#print("---------")
time = 0
i = 0
ret = {}
while True:
  if times_queue.empty():
    break
  d = times_queue.get()
  n = names_queue.get()
# print("%s %d" %(n,d))
# print(d)
  if d-q <= 0:
    time += d
    ret[n] = time
  else:
    times_queue.put(d-q)
    names_queue.put(n)
    time += q
#print("--------")
for key,value in ret.items():
  print("%s %d" %(key,value))

