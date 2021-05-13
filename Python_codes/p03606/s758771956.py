N=int(input())
ans=0
p=[]
for i in range(N):
    p.append(list(map(int,input().split())))
for i in range(N):
    ans+=p[i][1]-p[i][0]+1
print(ans)