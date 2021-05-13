n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

x=sum(b)-sum(a)

if x<0:
    print("No")
elif x==0:
    if a==b:
        print("Yes")
    else:
        print("No")
else:
    if x%2==0 and sum(a)%2!=sum(b)%2:
        print("No")
    elif x%2==1 and sum(a)%2==sum(b)%2:
        print("No")
    else:
        cnt=0
        for i in range(n):
            if a[i]<b[i]:
                cnt+=(b[i]-a[i]+1)//2
        if cnt<=x:
            print("Yes")
        else:
            print("No")