from collections import deque

header = input().split(" ")
N = int(header[0])
q = int(header[1])

queue = deque([])

for i in range(N):
    row = input().split(" ")
    queue.append((row[0], int(row[1])))

totalTime = 0

while queue:
    task = queue.popleft()
    name = task[0]
    time = task[1]
    leftTime = time - q
    if leftTime > 0:
        totalTime += q
        queue.append((name, leftTime))
    else:
        totalTime += time
        print(name + " " + str(totalTime))
