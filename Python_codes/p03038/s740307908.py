n , m = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
bc=[]
for i in range(m):
    b , c = map(int, input().split())
    bc.append((b,c))
bc.sort(key = lambda x : x[1],reverse=True)

t=0
for i in range(m):
    b,c=bc[i]
    if t>=n:
        break
    if a[t]>=c:
        break
    for j in range(b):
        if a[t]<c:
            a[t]=c
            if t<n-1:
                t+=1
        else:
            break
print(sum(a))
