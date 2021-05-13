n,y=list(map(int,input().split()))

for i in range(n+1):
    for j in range(n+1-i):
        res=y-10000*i-5000*j-1000*(n-i-j)
        if res==0:
            print('{} {} {}'.format(i,j,n-i-j))
            exit(0)

print('-1 -1 -1')