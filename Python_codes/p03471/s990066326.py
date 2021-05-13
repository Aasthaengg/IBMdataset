N,Y=map(int,input().split())
ans=0

nax=Y//1000

if N==nax:
    print(0,0,nax)
    exit()
elif N>nax:
    print(-1,-1,-1)
    exit()
else:
    for i in range(nax//10+1):
        for j in range(nax//5+1):
            if nax-10*i-5*j>=0 and nax-9*i-4*j==N:
                print(i,j,nax-10*i-5*j)
                exit()
print(-1,-1,-1)