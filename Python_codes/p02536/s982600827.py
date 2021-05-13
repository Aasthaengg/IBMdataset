n,m=map(int,input().split())
data=list(range(n))
cnt=n-1
def find(x):
    if data[x]==x:
        return x
    else:
        data[x]=find(data[x])
        return data[x]
for i in range(m):
    a,b=map(int,input().split())
    a=find(a-1)
    b=find(b-1)
    if a!=b:
        data[a]=b
        cnt-=1
print(cnt)