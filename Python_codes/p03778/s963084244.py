icase=0
if icase==0:
    w,a,b=map(int,input().split())
    if a+w<b:
        print(b-(a+w))
    elif b<=a+w and  a<=b+w:
        print(0)
    else:
        print(a-(b+w))
