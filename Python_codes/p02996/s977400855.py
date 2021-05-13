N = int(input())
tasks = [None] * N

for i in range(N):
  tasks[i] = tuple(map(int,input().split()))

tasks = sorted(tasks, key = lambda x:x[1])

time = 0
for t in tasks:
  if t[1] - t[0] < time:
    print("No")
    break
  time += t[0]
else:
  print("Yes")