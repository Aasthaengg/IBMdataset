n = int(input())
task = []
for _ in range(n):
    a, b = map(int, input().split())
    task.append((b, a))
task.sort()

time = 0
for b, a in task:
    time += a
    if time > b:
        print("No")
        quit()
print("Yes")