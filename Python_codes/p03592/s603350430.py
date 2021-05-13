n,m,k = map(int,input().split())
for i in range(0,n+1):
    for j in range(0,m+1):
        if (i*m + j*n) - (i*j)*2 == k:
            print("Yes")
            exit()
else:
    print("No")