# coding:utf-8
r,c = map(int, raw_input().split())
array = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    array[i] = map(int, raw_input().split())
for i in range(r):
    for j in range(c):
        print array[i][j],
    else:
        print sum(array[i])
total = 0
total2 = 0
for i in range(c):
    for j in range(r):
        total += array[j][i]
    else:
        print total,
        total2 += total
        total = 0
else:
    print total2

