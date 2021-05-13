# -*- coding: utf-8 -*-

A,B,Q = list(map(int, input().rstrip().split()))
s_list = [-10**11] + [int(input().strip()) for _ in range(A)] + [10**11]
t_list = [-10**11] + [int(input().strip()) for _ in range(B)] + [10**11]
x_list = [int(input().strip()) for _ in range(Q)]
#-----

# x_dic={ x : [a1,a2,b1,b2]}
#    距離xに対して、最も近い神社・寺のindexを保存
#      a1(xより西の最寄りの神社)、a2(xより東の最寄りの神社)
#      b1(xより西の最寄りの寺)、  b2(xより東の最寄りの寺)
x_dic={}

x_sort = sorted(x_list)

i_x=0
for i in range(len(s_list) - 1):
    
    while s_list[i] <= x_sort[i_x] <= s_list[i+1]:
        x_dic[x_sort[i_x]] = [i,(i+1)]
        i_x += 1
        
        if i_x > len(x_sort)-1: break
    if i_x > len(x_sort)-1: break
    

i_x=0
for i in range(len(t_list) - 1):
    
    while t_list[i] <= x_sort[i_x] <= t_list[i+1]:
        x_dic[x_sort[i_x]].extend( [i,(i+1)] )
        i_x += 1
        
        if i_x > len(x_sort)-1: break
    if i_x > len(x_sort)-1: break


for x in x_list:
    dist_min=10**11
    
    for s in x_dic[x][0:2]:
        for t in x_dic[x][2:4]:
            diff1 = abs(s_list[s] - x) + abs(t_list[t] - s_list[s])
            diff2 = abs(t_list[t] - x) + abs(s_list[s] - t_list[t])
            dist_min = min(dist_min, diff1, diff2)
    
    print(dist_min)
