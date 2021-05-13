n = int(input())
ans = n

if 8 < n:
    num = 8
    ans = 8
    add = 1
    flag = 0
    
    while 1:
        add *= 10
        
        for i in range(9):
            num += add
            ans += 1
            
            if n <= num:
                flag = 1
                break
                
        if flag == 1:
            break
            
print(ans)