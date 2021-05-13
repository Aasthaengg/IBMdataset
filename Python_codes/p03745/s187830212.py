n = int(input())
lis = list(map(int, input().split()))

cnt = 1

flag = 0
for i in range(n-1):
    if lis[i+1] - lis[i] >0:
        if flag == 1:
            pass
        elif flag == -1:
            flag = 0
            cnt += 1
        elif flag == 0:
            flag = 1
    elif lis[i+1] - lis[i] < 0:
        if flag == 1:
            flag = 0
            cnt += 1
        elif flag == -1:
            pass
        elif flag == 0:
            flag = -1
    elif lis[i+1] - lis[i] == 0:
        pass
    

print(cnt)