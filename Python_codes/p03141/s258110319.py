N=int(input())
AB=[]
for _ in range(N):
    a,b=map(int,input().split())
    AB.append([a+b,a,b])
AB.sort(reverse=True)

ans=0
for i in range(N):
    if i%2==0:
        ans+=AB[i][1]
    else:
        ans-=AB[i][2]
print(ans)