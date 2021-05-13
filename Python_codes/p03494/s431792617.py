n=int(input())
a=list(map(int,input().split()))

cnt=0
while 1:
    for i in range(n):
        if a[i]%2:
            print(cnt)
            exit()
    else:
        cnt+=1
        for i in range(n):
            a[i]//=2