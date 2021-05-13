n,m,k=map(int,input().split())
for x in range(n+m+1):
    for a in range(min(n+1,x+1)):
        if 0<=x-a<=m:
            num=a*m+(x-a)*(n-2*a)
            if k==num:
                print("Yes")
                exit()
print("No")
