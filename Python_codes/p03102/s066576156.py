N,M,C=map(int,input().split())
B=list(map(int,input().split()))
ans=0
for i in range(N):
    if sum(map(lambda x,y: int(x)*y, input().split(),B))+C>0:
        ans+=1
print(ans)