n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))
now=-100000000000
for i in range(1,n+1):
    retu=[]
    sum1=0
    sum2=0
    sum3=0
    max1=-1000000000000
    max2=-1000000000000
    flag=0
    x=i
    while(flag==0):
        x=p[x-1]
        sum1+=c[x-1]
        retu.append(c[x-1])
        if x==i:
            flag=1
    if len(retu)>=k: #操作回数が周期未満
        for j in range(k):
            sum2+=retu[j]
            if sum2>max1:
                max1=sum2
        ans=max1
    elif sum1<=0: #周期和が負
        for j in range(len(retu)):
            sum3+=retu[j]
            if sum3>max2:
                max2=sum3
        ans=max2
    else:
        w=k%len(retu)
        
        if w==0:
            w=len(retu)
        for j in range(w):
            sum2+=retu[j]
            if sum2>max1:
                max1=sum2
        for j in range(len(retu)):
            sum3+=retu[j]
            if sum3>max2:
                max2=sum3
        if max1+sum1>max2:
            ans=sum1*(k-w)//len(retu)+max1
        else:
            ans=sum1*((k-w)//len(retu)-1)+max2
    now=max(now,ans)
print(now)