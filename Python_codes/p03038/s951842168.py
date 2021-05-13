n,m=map(int, input().split())
a=list(map(int,input().split()))
a.sort()
cb=[0]*m
for i in range(m):
    b,c=map(int, input().split())
    cb[i]=(c,b)
cb.sort(reverse=True)

i=0
for j in range(m):
    for k in range(cb[j][1]):
        a[i]=max(cb[j][0],a[i])
        i+=1
        if i>=n:
            break
    else:
        continue
    break
print(sum(a))