import math

n, k = map(int,input().split())
l = list(map(int,input().split()))

ans = float('inf')

for i in range(k-1,n):
    bns=min(abs(l[i]-l[i-k+1])+abs(l[i]),abs(l[i]-l[i-k+1])+abs(l[i-k+1]))
    ans=min(ans,bns)
print(ans)
