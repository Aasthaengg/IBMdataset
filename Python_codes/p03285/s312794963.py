N = int(input())
flg = False
i = 0
while 7 * i <= N:
    j = 0
    while 7 * i + 4 * j <= N:
        if 7 * i + 4 * j == N:
            flg = True
            break
        j += 1
    if flg:
        break
    i += 1
if flg:
    print('Yes')
else:
    print('No')