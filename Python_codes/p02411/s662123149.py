while 1:
    m,f,r=map(int,raw_input().split())
    if m+f+r==-3:break
    if min(m,f)==-1 or m+f<30:print'F'
    elif m+f>=80:print'A'
    elif m+f>=65:print'B'
    elif max(m+f,r)>=50:print'C'
    else:print'D'