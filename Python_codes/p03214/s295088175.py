N=int(input())
a=list(map(int,input().split()))

avg= sum(a)/N
sabun=sum(a)
ans=0
for j in range(N):
    if abs(a[j]-avg) < sabun:
        ans=j
        sabun = abs(a[j]-avg)

print(ans)
