a,b,x = map(int,input().split())
t = b//x
if a == 0:
    print(t+1)
else:
    print(t-(a-1)//x)