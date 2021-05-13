N=int(input())
a = list(map(int,input().split()))

x = {}

for i in range(N):
    if a[i] in x:
        x[a[i]]=x[a[i]]+1
    else:
        x[a[i]]=1


ans = 0
for k in x:
    if(x[k]>=k):
        ans+=x[k]-k
    else:
        ans+=x[k]


print(ans)