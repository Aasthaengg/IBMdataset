while True:   
    n = int(input())
    if n ==0:
        break
    s_list=list(map(float,input().split()))
    
    m = (sum(s_list))/n
    
    ss = 0
    for i in s_list:
        si =((i-m)**2)
        ss += si  
    print((ss/n)**0.5) 
