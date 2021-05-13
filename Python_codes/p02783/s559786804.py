h,a=map(int,input().split())
n=0
while h>0:
    h-=a
    n+=1
    if h<=0:
        print(n)