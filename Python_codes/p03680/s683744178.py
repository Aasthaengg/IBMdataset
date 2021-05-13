N = int(input())
l = [(int(input())-1) for _ in range(N)]
flag = [0]*N
flag[0] = 1
flag[1] = 2
cnt = 0
cur_b = 0
while True:
    cnt += 1
    next_b = l[cur_b]
    if flag[next_b] == 1:
        print(-1)
        break
    elif flag[next_b] == 2:
        print(cnt)
        break
    else:
        flag[next_b] = 1
        cur_b = next_b
else:print(-1)        
