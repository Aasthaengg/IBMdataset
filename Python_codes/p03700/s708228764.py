n,a,b=map(int,input().split())
c=a-b
h=[int(input()) for i in range(n)]
low=1
high=10**9+1
while high-low>0:
    k=(high+low)//2
    count=0
    for u in h:
        u-=b*k
        if u>0:
            if u%c==0:
                count+=u//c
            else:
                count+=u//c+1
    if high-low==1:
        if count<=k:
            print(k)
            break
        else:
            print(k+1)
            break
    else:
        if count<=k:
            high=k
        else:
            low=k      