n,y = map(int,input().split())

for i in range(min(y//10000+1,n+1)):
    for j in range(min((y-10000*i)//5000+1,n-i+1)):
        k=n-i-j
        if i*10000+j*5000+k*1000==y and i+j+k==n:
            print(i,j,k);exit()
else:
    print(-1,-1,-1)