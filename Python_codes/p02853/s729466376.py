x,y=map(int,input().split())
def money(a):
    if a==1:
        return 300000
    elif a==2:
        return 200000
    elif a==3:
        return 100000
    else:
        return 0

ans=money(x)+money(y)
if ans==600000:
    print(1000000)
else:
    print(ans)
