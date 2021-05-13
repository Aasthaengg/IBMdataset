n = int(input())

t = 0
task = []
for i in range(n):
    a,b = map(int,input().split())
    task.append([b,a])

task.sort()
ans = "Yes"
for i in range(n):
    t += task[i][1]
    if task[i][0] < t:
        ans = "No"
        break

print(ans)