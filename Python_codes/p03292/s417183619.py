from math import fabs

A_num = list(map(int, input().split()))

def func(a,b,c):
    cost = 0
    cost += fabs(A_num[b]-A_num[a])
    cost += fabs(A_num[c]-A_num[b])

    return cost

print(int(min(func(0,1,2),func(0,2,1),func(1,0,2),func(1,2,0),func(2,0,1),func(2,1,0))))