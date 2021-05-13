n=int(input())
a=list(map(int,input().split()))
num=[0]*8
up2800=0
for i in range(n):
    if a[i]<400:
        num[0]+=1
    elif a[i]<800:
        num[1]+=1
    elif a[i]<1200:
        num[2]+=1
    elif a[i]<1600:
        num[3]+=1
    elif a[i]<2000:
        num[4]+=1
    elif a[i]<2400:
        num[5]+=1
    elif a[i]<2800:
        num[6]+=1
    elif a[i]<3200:
        num[7]+=1
    else:
        up2800+=1
num2=8-num.count(0)
if num2==0:
    print(1,up2800)
else:
    print(num2,num2+up2800)
