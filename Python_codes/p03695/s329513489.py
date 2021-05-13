n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    if a[i]<400:
        l.append("hai")
    elif a[i]<800:
        l.append("cha")
    elif a[i]<1200:
        l.append("midori")
    elif a[i]<1600:
        l.append("mizu")
    elif a[i]<2000:
        l.append("ao")
    elif a[i]<2400:
        l.append("ki")
    elif a[i]<2800:
        l.append("orange")
    elif a[i]<3200:
        l.append("red")
    else:
        l.append("free")
ls=set(l)
if "free" not in ls:
    print(len(ls),len(ls))
else:
    x=len(ls)-1#free以外の色の数
    y=x+l.count("free")
    #if y>8:
        #y=8
    
    if x==0:
        x=1
    print(x,y)