n=int(input())
lst_to=[[] for i in range(n**2)]
lst_from=[[] for i in range(n**2)]
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(n-2):
        i1=i
        i2=i
        b=a[j]-1
        c=a[j+1]-1
        if i1>b:
            i1,b=b,i1
        if i2>c:
            i2,c=c,i2
        lst_to[n*i1+b].append(n*i2+c)
        lst_from[n*i2+c].append(n*i1+b)

que=[]
for i in range(n):
    for j in range(i+1,n):
        if not lst_from[n*i+j]:
            que.append(n*i+j)

count=0
while que:
    count+=1
    h=[]
    for u in que:
        for v in lst_to[u]:
            lst_from[v].remove(u)
            if not lst_from[v]:
                h.append(v)
    que=h

for i in range(n):
    for j in range(i+1,n):
        if lst_from[n*i+j]:
            print(-1)
            break
    else:
        continue
    break
else:
    print(count)