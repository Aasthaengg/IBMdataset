N=int(input())
p=list(map(int, input().split()))
ans=0
flag=0
for i in range(N):
    if i+1==p[i] and flag==0:
        ans+=1
        flag=1
    elif flag==1:
        flag=0
print(ans)