N=int(input())
a=list(map(int,input().split()))

d={}
for h in range(1,N):
    if a[h] in d:
        d[a[h]]+=1
    else:
        d[a[h]]=1
ans="Yes"
b=[a[0]]

for h in range(1,N):
    t=a[h]^a[0]
    if t in d:
        b.append(a[h])
        d[a[h]]-=1
        if d[a[h]]==0:
            del d[a[h]]
        break
    if h==N-1:
        ans="No"

if ans=="Yes":
    for i in range(1,N+1):
        if i==h:
            continue
        if i==N:
            t=b[-1]^b[-2]
            if t!=b[0]:
                ans="No"
            break
        t=b[-1]^b[-2]
        if t in d:
            b.append(t)
            d[t]-=1
            if d[t]==0:
                del d[t]
        else:
            ans="No"
            break

print(ans)