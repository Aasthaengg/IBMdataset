n,m= map(int,input().split())
l = []
for i in range(m):
    a=(list(map(int,input().split())))
    l.append(a[1:])
b = list(map(int,input().split()))
ans = 0
for i in range(2**n):
    sw = [0 for i in range (m)]
    g = i+0
    for j in range(n):
        if g &1 == True:
            for k in range(m):
                if j+1 in l[k]:
                    sw[k]+=1
        g = g>>1
    cnt = 0
    for j in range(m):
        if sw[j]%2==b[j]:
            cnt+=1
    if cnt==m:
        ans+=1
print(ans)