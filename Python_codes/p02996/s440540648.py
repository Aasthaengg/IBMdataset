n = int(input())
tasks = []

for i in range(n):
    ai, bi = list(map(int, input().split()))
    tasks.append((ai, bi))

tasks = sorted(tasks, key=lambda x: x[1])

t = 0
for i in range(n):
    if t > tasks[i][1] - tasks[i][0]:
        print("No")
        exit()
    else:
        t += tasks[i][0]

print("Yes")