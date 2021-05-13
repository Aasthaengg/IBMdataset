n,m=map(int,input().split())
p=list(int(i)-1 for i  in input().split())
s=[list(int(i)-1 for i  in input().split()) for _ in range(m)]

a={i:i for i in range(n)}

def find(x):
    if a[x]==x:
        return x
    else:
        a[x]=find(a[x])
        return a[x]

for x,y in s:
    a[find(x)] = find(y)

ans=0

for i in range(n):
    if find(i)==find(p[i]):
        ans+=1


print(ans)