n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
kai=sum(b)-sum(a)
if kai<0:
    for i in range(n):
        if a[i]!=b[i]:print("No");exit()
    print("Yes")
else:
    akai=kai
    bkai=kai
    for i in range(n):
        if a[i]==b[i]:continue
        if a[i]>b[i]:
            bkai-=a[i]-b[i]
        else:
            if (b[i]-a[i])%2:
                b[i]+=1
                bkai-=1
            akai-=(b[i]-a[i])//2
        if akai<0 or bkai<0:print("No");exit()
    print("Yes")if bkai==2*akai else print("No")


