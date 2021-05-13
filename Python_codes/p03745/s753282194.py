n=int(input())
a=list(map(int, input().split()))

if n<=2:
    print(1)
else:
    status="U"
    for i in range(n):
        if a[i+1]-a[i]<0:
            status="D"
            break
        elif a[i+1]-a[i]>0:
            status="U"
            break

    cnt=1
    reset_flag=False
    for i in range(n-1):
        if reset_flag:
            if a[i+1]-a[i]>0:
                status="U"
                reset_flag=False
            elif a[i+1]-a[i]<0:
                status="D"
                reset_flag=False
            else:
                continue
        elif status=="D" and a[i+1]-a[i]>0:
            cnt+=1
            reset_flag=True
        elif status=="U" and a[i+1]-a[i]<0:
            cnt+=1
            reset_flag=True
    print(cnt)

