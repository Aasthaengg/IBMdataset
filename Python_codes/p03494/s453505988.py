nn = int(input())
dd = list(map(int,input().split()))
nof_op = 0
finish = 0
while True:
    for ind in range(nn):
        if (dd[ind] % 2) == 1:
            finish = 1
            break
        else:
            dd[ind] = dd[ind] / 2
    if finish == 1:
        break
    else:
        nof_op += 1
print(nof_op)