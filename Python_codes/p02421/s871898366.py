# coding:utf-8
n = input()
taro_cnt = 0
hanako_cnt = 0
taro = ["" for i in range(n)]
hanako = ["" for i in range(n)]
for i in range(n):
    split = raw_input().split()
    taro[i] = split[0]
    hanako[i] = split[1]
for i in range(n):
    if taro[i] > hanako[i]:
        taro_cnt += 3
    elif taro[i] < hanako[i]:
        hanako_cnt += 3
    else:
        taro_cnt += 1
        hanako_cnt += 1
else:
    print taro_cnt,hanako_cnt

