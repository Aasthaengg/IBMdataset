icase=0
if icase==0:
    a,b,c=map(int,input().split())
    k=int(input())
    xmax=max(a,b,c)
    xx=xmax*2**k+a+b+c-xmax
    print(xx)
