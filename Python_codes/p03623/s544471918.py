icase=0    
if icase==0:
    x,a,b=map(int,input().split())
    if abs(a-x)<abs(x-b):
        print("A")
    else:
        print("B")