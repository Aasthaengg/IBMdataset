N = int(input())
tsk = [list(map(int, input().split())) for _ in range(N)]

tsk.sort(key=lambda x: x[1])
cnt = 0
A = [0]

for i in range(N):
    cnt += tsk[i][0]
    if cnt > tsk[i][1]:
        print("No")
        exit()
print("Yes")
#print(tsk)   