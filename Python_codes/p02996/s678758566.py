from collections import deque
n = int(input())
task = deque()
now = 0
for i in range(n):
  task.append(tuple(map(int, input().split())))
task = deque(sorted(task, key = lambda x: x[1]))
while True:
  work = task.popleft()
  now+=work[0]
  if now>work[1]:
    print('No')
    break
  if len(task) == 0:
    print('Yes')
    break