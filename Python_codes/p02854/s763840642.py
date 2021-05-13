n=int(input())
A=list(map(int,input().split()))
ans=float('INF')
sa=[0]
for i,a in enumerate(A):
    sa.append(sa[i]+a)
for i in range(n+1):
    ans=min(ans,abs(sa[i]-(sa[-1]-sa[i])))
print(ans)