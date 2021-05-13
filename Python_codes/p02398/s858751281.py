# coding:utf-8
array = map(int, raw_input().split())
cnt = 0
for i in range(array[0],array[1] + 1):
    if array[2] % i == 0:
        cnt += 1
else:
    print cnt