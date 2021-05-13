n,m=map(int,input().split())
l=[0]*(n+1)
for i in range(m):
    a,b=[int(j) for j in input().split()]
    l[a]=(l[a]+1)%2
    l[b]=(l[b]+1)%2
if sum(l)==0:
    print("YES")
else:
    print("NO")