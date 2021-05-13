n=int(input())
k=[[0,0] for i in range(n)]
for i in range(n):
    a,l=map(int,input().split())
    left=a-l
    right=a+l
    k[i][0]=left
    k[i][1]=right
k.sort(key=lambda x:x[1])
tmp=k[0][1]
ans=1
for i in range(n):
    if k[i][0]>=tmp:
        tmp=k[i][1]
        ans+=1
print(ans)