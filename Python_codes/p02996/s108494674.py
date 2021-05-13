N = int(input())
job = [list(map(int, input().split())) for _ in range(N)]
job.sort(key=lambda x: x[1])
time = 0
FLG = True

for need, limit in job:
    time += need
    if time > limit:
        FLG = False
        break

if FLG:
    print("Yes")
else:
    print("No")
