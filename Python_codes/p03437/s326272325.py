x,y=map(int,input().split())
if x%y==0:
    print(-1)
else:
    for i in range(1,y):
        tmp = x*i
        if tmp%y!=0:
            print(tmp)
            exit()
    print(-1)
