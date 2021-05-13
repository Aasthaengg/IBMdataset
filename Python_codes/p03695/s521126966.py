n=int(input())
a=list(map(int,input().split()))
k=[0]*8
s=0
for i in a:
    if i<400:
        k[0]+=1
    elif i<800:
        k[1]+=1
    elif i<1200:
        k[2]+=1
    elif i<1600:
        k[3]+=1
    elif i<2000:
        k[4]+=1
    elif i<2400:
        k[5]+=1
    elif i<2800:
        k[6]+=1
    elif i<3200:
        k[7]+=1
    else:
        s+=1
if k.count(0)==8:
    b=1
    c=s
    print(str(b)+" "+str(c))
else:
    b=8-k.count(0)
    c=b+s
    print(str(b)+" "+str(c))