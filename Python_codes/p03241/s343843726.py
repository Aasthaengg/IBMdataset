n,m=map(int,input().split())
t=int(m/n)
while True:
    if m%t==0:
        if t*n<=m:
            print(t)
            exit()
        else:
            t-=1
    else:
        t-=1