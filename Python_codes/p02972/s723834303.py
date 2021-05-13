n=int(input())
a=[0]+[int(x) for x in input().split()]
boal=[0]*(n+1)
m=0
ans=[]
for i in range(n,0,-1):
    k=1
    sum_boal=0
    while i*k<n+1:
        sum_boal+=boal[i*k]
        k+=1
    if sum_boal%2!=a[i]:
        boal[i]+=1
        m+=1
        ans.append(i)
print(m)
print(*ans)