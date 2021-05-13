N,K = map(int,input().split())
count = 0
another = 0
if(K%2==1):
    for i in range(1,N+1):
        if(i%K==0):
            count+=1
    print(count**3)
else:
    for i in range(1,N+1):
        if(i%K==0):
            count+=1
        elif(i%K==(K//2)):
            another+=1
    print((count)**3+(another)**3)