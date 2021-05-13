# -*- coding: utf-8 -*-

N = int(input())
conditions = []
for i in range(N):
    x,y,h = map(int, input().split())
    conditions.append([x,y,h])


for cx in range(101):
    for cy in range(101):
        H = -1
        for _,cond in enumerate(conditions):
            if cond[2] > 0:
                H_tmp = cond[2] + abs(cond[0]-cx) + abs(cond[1]-cy)
                if H == -1:
                    H = H_tmp
                else:
                    if H_tmp != H:
                        H = -2
                        break

        if H == -2:
            continue

        for _,cond in enumerate(conditions):
            if cond[2] == 0:
                if H > abs(cond[0]-cx) + abs(cond[1]-cy):
                    H = -2
                    break
        
        if H == -2:
            continue
        
        print(cx,cy,H)

