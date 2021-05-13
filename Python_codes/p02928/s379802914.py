mod=10**9+7

n,k = map(int,input().split())
l = list(map(int,input().split()))
l2 = l+l

x=0
for i in range(n-1):
    for j in range(i,n-1):
        if l[i] > l[j+1]:
                x+=1

y=0
for i in range(2*n-1):
    for j in range(i,2*n-1):
        if l2[i] > l2[j+1]:
                y+=1

y-=(2*x)

tmp = (k*(k-1)//2)%mod
ans = ((tmp*y)%mod + (x*k)%mod)%mod
print(ans)