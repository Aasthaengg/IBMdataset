n,m=map(int,input().split())
 
a=[int(i) for i in range(n)]

def find(a, x):
    if a[x] != x:
        a[x] = find(a, a[x])
    return a[x]
def unite(a, x, y):
    x = find(a, x)
    y = find(a, y)
    if x != y:
        a[x] = min(x, y)
        a[y] = a[x]
p=list(int(i)-1 for i  in input().split())
pp=p
ans=0
#007映画　4/10
s=[list(int(i)-1 for i  in input().split()) for _ in range(m)]
for x, y in s:
    unite(a,x,y)
for i in range(n):
    if find(a,i)==find(a,pp[i]):
        ans+=1

print(ans)