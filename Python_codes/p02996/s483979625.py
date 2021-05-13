from sys import exit

n = int(input())
job = [list(map(int, input().split())) for _ in range(n)]

job.sort(key=lambda x: x[1])
time = 0
for a, b in job:
    time += a
    if time > b:
        print('No')
        exit()
print('Yes')