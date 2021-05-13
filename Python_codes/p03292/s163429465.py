a1, a2, a3 = map(int, input().split())
task = [a1, a2, a3]
task.sort()
print(task[1]-task[0] + task[2]-task[1])
