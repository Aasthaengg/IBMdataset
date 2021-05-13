n,y = map(int,input().split())

for i in range(0,n+1):
    for j in range(0,n+1-i):
        k = max(0,n-i-j)
        if 10000*i + 5000*j + 1000*k == y:
            print(i,j,k)
            exit(0)

print(-1,-1,-1)