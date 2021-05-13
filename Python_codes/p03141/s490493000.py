N=int(input())
l=[]
for i in range(N):
    A,B=map(int,input().split())
    l.append((A,B))
l.sort(reverse=True,key=lambda x:(x[0]+x[1],x[0]))
ans=0
for i,e in enumerate(l):
    if i%2==0:
        ans+=e[0]
    elif i%2==1:
        ans+=-e[1]
print(ans)