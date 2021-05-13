N = int(input())
ABs = [list(map(int, input().split())) for _ in range(N)]
ABs = sorted(ABs, key = lambda x:x[1])

now_index = 0
now_time = 0
while now_index < N:
    deadline = ABs[now_index][1]
    now_time += ABs[now_index][0]
    additional_task = 0
    for i in range(now_index+1, N):
        if ABs[i][1] != deadline:
            break
        else:
            now_time += ABs[i][0]
            additional_task+=1
    now_index += 1
    now_index += additional_task
    if now_time > deadline:
        print("No")
        break
else:
    print("Yes")