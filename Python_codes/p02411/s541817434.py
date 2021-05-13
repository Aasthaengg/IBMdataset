def evl_score(m,f,r):
    if m == -1 or f == -1:
        ret = 'F'
    elif m + f >= 80:
        ret = 'A' 
    elif m + f >= 65 and m + f < 80:
        ret = 'B' 
    elif m + f >= 50 and m + f < 65: 
        ret = 'C' 
    elif m + f >= 30 and m + f < 50: 
        if r >= 50: 
            ret = 'C' 
        else:
            ret = 'D' 
    else: 
        ret = 'F'
    return ret 
while True:
    m,f,r =[int(i) for i in input().split(' ')] 
    if (m == -1 and f == -1 and r == -1):
        break 
    print(evl_score(m,f,r)) 
