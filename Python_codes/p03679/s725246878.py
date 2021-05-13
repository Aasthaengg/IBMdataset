icase=0    
if icase==0:
    x,a,b=map(int,input().split())
    if b-a<=0:    
        print("delicious")
    elif b-a<=x:    
        print("safe")
    else:
        print("dangerous")