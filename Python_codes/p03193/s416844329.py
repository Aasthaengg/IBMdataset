N,H,W= map(int,input().split())
a = [[]*N]*N
for i in range(N):
    a[i]=input().rstrip().split()


count=0
for i in range(0,N):
    if ((int(a[i][0])>=H)and(int(a[i][1])>=W)):
        count+=1


print(count)