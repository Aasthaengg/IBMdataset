x = str(input())
cnt = 0
tmp = 0
for i in x:
    if i == 'T':
        if tmp > 0:
            tmp -= 1
        else:
            cnt += 1
    else:
        tmp += 1
else:
    print(cnt + tmp)
