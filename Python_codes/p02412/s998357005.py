# coding: utf-8
while True:
    n,x = map(int, input().split())
    
    if n == x == 0:
        break
    
    list = [i for i in range(1,n+1)]
    count = 0
    
    for i in list:
        for j in list[i:]:
            k = x - (i + j)
            if list[j:].count(k) == 1:
                count += 1
                
    print(count)