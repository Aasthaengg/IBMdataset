N = int(input())
task = [0]*N
for i in range(N):
    a, b = map(int,input().split())
    task[i] = (b, a)
task.sort()

#print(task)

time = 0
for t in task:
    limit, required = t
    if time + required > limit:
        print('No')
        break
    time += required
else:
    print('Yes')