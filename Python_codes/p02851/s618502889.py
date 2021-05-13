import collections

n,k=map(int,input().split())
a=list(map(int,input().split()))
sa = [0]
for i in range(n):
    sa.append(sa[i]+a[i])
    sa[i+1] -= 1
    sa[i+1] %= k
cd = collections.defaultdict(lambda:0)
res = 0
for i in range(n+1):
    cd[sa[i]] += 1
    if i >= k:
        cd[sa[i-k]] -= 1
    res += cd[sa[i]] - 1
print(res)