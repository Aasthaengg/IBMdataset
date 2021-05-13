n = int(input())
a = list(map(int,input().split()))

a.sort()

u,d,z = 0,0,0
uu,dd = [],[]
for i in range(n):
    if a[i] > 0:
        u += 1
        uu.append(a[i])
    elif a[i] < 0:
        d += 1
        dd.append(a[i])
    else:
        z += 1
        
dd = dd[::-1]
        
ans = []
if u == 0 and d == 0:
    for i in range(z-1):
        ans.append((0,0))
    cur = 0
    
elif d == 0:
    if z != 0:
        for i in range(z-1):
            ans.append((0,0))
        cur = 0
        for i in range(u-1):
            ans.append((cur,uu[i]))
            cur -= uu[i]
        ans.append((uu[u-1],cur))
        cur = uu[u-1] - cur
    else:
        cur = uu[0]
        for i in range(u-2):
            ans.append((cur,uu[i+1]))
            cur -= uu[i+1]
        ans.append((uu[u-1],cur))
        cur = uu[u-1] - cur
        
elif u == 0:
    if z != 0:
        for i in range(z-1):
            ans.append((0,0))
        cur = 0
        for i in range(d):
            ans.append((cur,dd[i]))
            cur -= dd[i]
    
    else:
        cur = dd[0]
        for i in range(d-1):
            ans.append((cur,dd[i+1]))
            cur -= dd[i+1]
            
else:
    for i in range(z):
        ans.append((uu[0],0))
    cur1 = uu[0]
    cur2 = dd[0]
    for i in range(d-1):
        ans.append((cur1,dd[i+1]))
        cur1 -= dd[i+1]
    for i in range(u-1):
        ans.append((cur2,uu[i+1]))
        cur2 -= uu[i+1]
        
    ans.append((cur1,cur2))
    cur = cur1 - cur2
    
print(cur)
for i in ans:
    print(*i)