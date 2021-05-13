a,b,x=map(int,input().split())
start=((a-1)//x+1)*x
if start>b:
    print(0)
else:
    print((b-start)//x+1)