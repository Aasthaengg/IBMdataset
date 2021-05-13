import itertools

n,m,k = map(int,input().split())
a = list(map(int,('0 '+input()).split()))
b = list(map(int,('0 '+input()).split()))

asum = list(itertools.accumulate(a))
bsum = list(itertools.accumulate(b))

ans = 0
j=m
for i in range(n+1):
    if asum[i]>k:
        break
    
    while asum[i]+bsum[j]>k:
        j-=1
        
    ans = max(ans,i+j)

print(ans)