#abc056 b 
w,a,b=map(int,input().split())
if a>b:
    tmp=a 
    a=b 
    b=tmp 
if b<a+w:
    print(0)
else:
    print(b-a-w)