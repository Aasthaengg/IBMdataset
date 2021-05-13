a,b,c=(int(x) for x in input().split())
ireru=a-b#cが入れる量
if (c-ireru<0):
    print(0)
else:
    print(c-ireru)