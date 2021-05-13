w,a,b=map(int,input().split())
if a>b:
    a,b=b,a
    #swapped 
if a+w>=b:
    print(0)
else:
    print(b-(a+w))
