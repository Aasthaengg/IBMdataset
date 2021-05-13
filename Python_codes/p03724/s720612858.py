n,m=map(int,input().split())
l=[0]*(n+1)
ku=[]
for _ in range(m):
    ku.append(tuple(map(int,input().split())))
for x in ku:
    a,b=x
    l[a]=(l[a]+1)%2
    l[b]=(l[b]+1)%2
print("NO" if 1 in l else "YES")