icase=0    
if icase==0:
    a,b,c=map(int,input().split())
    print(min(a+b,b+c,c+a))