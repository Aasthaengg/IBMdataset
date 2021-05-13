n = int(input())
a = list(map(int,input().split()))
up=0
down=0
cnt=0
for i in range(n-1):
    if up==1:
        if a[i]>a[i+1]:
            up=0
            cnt+=1
    elif down==1:
        if a[i]<a[i+1]:
            down=0
            cnt+=1
    else:
        if a[i]<a[i+1]:
            up=1
        elif a[i]>a[i+1]:
            down=1
else:
    cnt+=1
    print(cnt)