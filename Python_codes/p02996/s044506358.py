N = int(input())
T = list()
for _ in range(N):
    a, b = map(int, input().split())
    T.append((a, b))
T = sorted(T, key=lambda x:x[1])

Time = 0 
for task in T:
    taskTime, deadline = task
    Time += taskTime
    if deadline < Time:
        print("No")
        exit()
print("Yes")

