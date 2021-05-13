n = int(input())
eight_cnt = 0

for i in range(1, n + 1, 2):
    j = 1
    cnt = 0
    
    while j*j <= i :
        if i % j == 0 :
            if j*j == i :
                cnt += 1
                
            else:
                cnt += 2
                
        j += 1
        
    if cnt == 8 :
        eight_cnt += 1
        
print(eight_cnt)  