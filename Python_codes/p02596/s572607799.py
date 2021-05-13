k=int(input())
if k%2==0:
    print(-1)
else:
    n=7
    cnt=1
    l={}
    while n%k!=0:
        if n not in l:
            l[n]=1
        else:
            print(-1)
            exit()
        n=(n*10+7)%k
        cnt+=1
    print(cnt)