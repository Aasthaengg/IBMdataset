# -*- coding: utf-8 -*-

N = int(input().strip())
A_list = list(map(int, input().rstrip().split()))
#-----

S=0
for i in range( len(A_list) ):
    if i==0:
        S = abs(A_list[i])
    else:
        S += abs(A_list[i] - A_list[i-1])
        
S += abs(A_list[i])


ans_S=[]
for i in range( len(A_list) ):
    if i == 0:
        ex_S = S - abs(A_list[i+1] - A_list[i]) - abs(A_list[i] - 0) + abs(A_list[i+1] - 0)
    elif i == len(A_list)-1:
        ex_S = S - abs(0 - A_list[i]) - abs(A_list[i] - A_list[i-1]) + abs(0 - A_list[i-1])
    else:
        ex_S = S - abs(A_list[i+1] - A_list[i]) - abs(A_list[i] - A_list[i-1]) + abs(A_list[i+1] - A_list[i-1])
    
    ans_S.append(ex_S)


for i in ans_S:
    print(i)
