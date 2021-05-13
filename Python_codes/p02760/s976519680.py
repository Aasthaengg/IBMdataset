bingo = [list(map(int, input().split())) for _ in range(3)]
def chec_line():
    ret = False
    for i in range(3):
        cnt = 0
        for j in range(3):
            if bingo[i][j] == -1:
                cnt += 1
        if cnt == 3:
            ret =True

    for i in range(3):
        cnt = 0
        for j in range(3):
            if bingo[j][i] == -1:
                cnt += 1
        if cnt == 3:
            ret =True
    cnt = 0
    for i in range(3):
        if bingo[i][i] == -1:
            cnt += 1
    if cnt == 3:
        ret =True
    
    cnt = 0
    for i in range(3):
        if bingo[2-i][i] == -1:
            cnt += 1
    if cnt == 3:
        ret =True

    return ret
def check_num( num):
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == num:
                bingo[i][j] = -1
                

n = int(input())
flag = False
for _ in range(n):
    check_num(int(input()))
    flag = chec_line() 
    if flag:
        break
if flag :
    print('Yes')
else:
    print('No')