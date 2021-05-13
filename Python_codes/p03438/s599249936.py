n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

aPlus=0
bPlus=0

for i in range(n):
    if a[i]>b[i]:
        aPlus+=(a[i]-b[i])
    elif a[i]<b[i]:
        if (b[i]-a[i])%2==0:
            bPlus+=(b[i]-a[i])//2
        else:
            aPlus+=1
            bPlus+=(b[i]+1-a[i])//2

if aPlus<=bPlus:
    print("Yes")
else:
    print("No")