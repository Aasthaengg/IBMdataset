n = int(input())
ls = list(map(int,input().split()))
cnt = 1
i = 0
flag = 10
while i < n-1:
    if ls[i] < ls[i+1] and flag == 10:
        flag = True
    elif ls[i] > ls[i+1] and flag == 10:
        flag = False
    if flag == True:
        if ls[i] > ls[i+1]:
            cnt += 1
            flag = 10
    elif flag == False:
        if ls[i] < ls[i+1]:
            cnt += 1
            flag = 10
    i += 1
print(cnt)