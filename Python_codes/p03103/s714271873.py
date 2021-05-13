n,m = map(int,input().split())
ans,a = 0,[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort()
for i in range(n):
    x = min(m,a[i][1])
    ans+=x*a[i][0]
    m-=x
    if m==0: break
print(ans)