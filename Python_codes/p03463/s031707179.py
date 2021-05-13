n,a,b=map(int,input().split())
m=[999]+[0 for i in range(n)]+[999]
m[a]=1
m[b]=2
cnt=0
while 1:
    if cnt%2==0:
        if m[a+1]==0:
            m[a]=0
            m[a+1]=1
            a+=1
        elif m[a-1]==0:
            m[a]=0
            m[a-1]=1
            a-=1
        else:
            print('Borys')
            exit()
    else:
        if m[b-1]==0:
            m[b]=0
            m[b-1]=1
            b-=1
        elif m[b+1]==0:
            m[b]=0
            m[b+1]=1
            b+=1
        else:
            print('Alice')
            exit()

    cnt+=1