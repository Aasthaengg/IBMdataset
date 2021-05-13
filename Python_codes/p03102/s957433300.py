n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[list(map(int,input().split())) for _ in range(n)]
cnt=0
for i in range(n):
    d=0
    for j in range(m):
        d+=a[i][j]*b[j]
    if d+c>0:
        cnt+=1
print(cnt)