h,a=map(int, input().split())
n=0

while 1:
    h-=a
    n+=1
    if h<=0:
        print(n)
        exit(0)