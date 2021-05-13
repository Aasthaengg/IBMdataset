n,y=map(int,input().split())
amari=y-1000*n

if amari < 0:
    print(-1,-1,-1)
    exit()

for k in range(0,n+1):
    if amari-4000*k >= 0 and (amari-4000*k)%5000 == 0:
        x=(amari-4000*k)//5000
        if k-x >= 0:
            y=k-x
            print(x,y,n-k)
            break
else:
    print(-1,-1,-1)