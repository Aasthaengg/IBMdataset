# -*- coding: utf-8 -*-

D,G = list(map(int, input().rstrip().split()))
pc_list = [list(map(int, input().rstrip().split())) for i in range(D)]
#-----

bit = 1 << D
min_cnt = 10*100

for b in range(bit):
    score = 0
    cnt = 0
    
    for i in range(D):
        if b & (1 << i):
            p = pc_list[i][0]
            c = pc_list[i][1]
            
            score += p * (100*(i+1)) + c
            cnt += p
    
    if score >= G:
        min_cnt = min(min_cnt, cnt)
    
    else:
        flag = False
        
        for i in reversed(range(len(pc_list))):
            if flag:
                break
            
            if b & (1 << i):
                continue
            
            p = pc_list[i][0]
            
            for j in range(p-1):
                score += 100*(i+1)
                cnt += 1
                
                if score >= G:
                    min_cnt = min(min_cnt, cnt)
                    flag = True
                    break

print(min_cnt)
