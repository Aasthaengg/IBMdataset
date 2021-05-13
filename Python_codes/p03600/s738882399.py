import sys
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
inf=float("inf")
data=[[inf]*n for i in range(n)]
ans=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==k or j==k:
                continue
            if a[i][j]==a[i][k]+a[k][j]:
                break
            elif a[i][j]>a[i][k]+a[k][j]:
                print(-1)
                sys.exit()
        else:
            data[i][j]=a[i][j]
            ans+=a[i][j]
print(ans//2)