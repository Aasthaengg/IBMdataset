n,h,w=map(int,input().split())
X=[list(map(int,input().split())) for _ in range(n)]
ans=0
for i in range(n):
    if X[i][0]>=h and X[i][1]>=w:
        ans+=1
print(ans)