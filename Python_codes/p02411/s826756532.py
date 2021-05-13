while 1:
    m,f,r=map(int,input().split())
    if m == -1 and f == -1 and r == -1: break
    if m == -1 or f == -1: s = 'F'
    elif m + f >= 80: s = 'A'
    elif m + f >= 65: s = 'B'
    elif m + f >= 50: s = 'C'
    elif m + f >= 30: 
        if r >= 50: s = 'C'
        else : s = 'D'
    else : s = 'F'
    print(s)