def resolve(x,y):
    if (x+y)%2 == 1:
        print((x+y+1)//2)
    else:
        print((x+y)//2)
a,b=map(int,input().split())
resolve(a,b)