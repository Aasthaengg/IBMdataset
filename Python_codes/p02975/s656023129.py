N=int(input())
a=list(map(int,input().split()))
x=set(a)
if len(x)==1:
    if 0 in x:
        ans=1
    else:
        ans=0
elif len(x)==2:
    if 0 in x:
        count0=0
        count1=0
        for i in range(len(a)):
            if a[i]==0:
                count0+=1
            else:
                count1+=1
        if count0*2==count1:
            ans=1
        else:
            ans=0
    else:
        ans=0
elif len(x)==3:
    y=list(x)
    t=y[0]^y[1]^y[2]
    if t==0:
        count0=0
        count1=0
        count2=0
        for i in range(len(a)):
            if a[i]==y[0]:
                count0+=1
            elif a[i]==y[1]:
                count1+=1
            else:
                count2+=1
        if count0==count1:
            if count1==count2:
                ans=1
            else:
                ans=0
        else:
            ans=0
    else:
        ans=0
else:
    ans=0
if ans:
    print("Yes")
else:
    print("No")