# -*- coding:utf-8 -*-
n,m,c = map(int,input().split())
b_list = list(map(int,input().split()))
a_list =[]
for i in range(n):
    a_list.append(list(map(int,input().split())))

ret_num = 0
sum = 0

for N in range(n):
    sum = 0
    for M in range(m):
        sum += a_list[N][M] * b_list[M]
    if sum + c > 0:
        ret_num += 1

print(ret_num)

        
