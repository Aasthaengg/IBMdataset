a,b,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=[0]*m
for i in range(m):
    x,y,c=map(int,input().split())
    ans[i]=a[x-1]+b[y-1]-c
ans.append(min(a)+min(b))
print(min(ans))